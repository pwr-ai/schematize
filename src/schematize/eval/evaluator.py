import json
from dataclasses import dataclass
from typing import Any, Literal

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field, create_model


class CoverageAssessment(BaseModel):
    is_covered: bool = Field(description="Whether the question is covered by the schema")
    confidence: Literal["high", "medium", "low"] = Field(
        description="Confidence level: high (clearly covered/not covered), medium (partially covered or unclear), low (uncertain)"
    )


@dataclass
class SchemaEvaluation:
    total_questions: int
    covered_questions: int
    high_confidence_coverage: int
    medium_confidence_coverage: int
    low_confidence_coverage: int


def _build_batch_model(n: int) -> type[BaseModel]:
    fields = {
        f"question_{i + 1}": (CoverageAssessment, Field(description=f"Assessment for question {i + 1}"))
        for i in range(n)
    }
    return create_model("BatchCoverageAssessment", **fields)


class SchemaEvaluator:
    def __init__(self, llm: BaseChatModel, evaluation_prompt: str):
        self.llm = llm
        self.evaluation_prompt_template = PromptTemplate.from_template(evaluation_prompt)

    def _build_chain(self, n: int):
        return self.evaluation_prompt_template | self.llm.with_structured_output(_build_batch_model(n))

    def _parse_assessments(self, result: Any, n: int) -> dict[str, CoverageAssessment]:
        return {f"question_{i + 1}": getattr(result, f"question_{i + 1}") for i in range(n)}

    def _tally(self, assessments: dict[str, CoverageAssessment]) -> SchemaEvaluation:
        covered_count = high_conf = medium_conf = low_conf = 0
        for assessment in assessments.values():
            if assessment.is_covered:
                covered_count += 1
                if assessment.confidence == "high":
                    high_conf += 1
                elif assessment.confidence == "medium":
                    medium_conf += 1
                elif assessment.confidence == "low":
                    low_conf += 1
        return SchemaEvaluation(
            total_questions=len(assessments),
            covered_questions=covered_count,
            high_confidence_coverage=high_conf,
            medium_confidence_coverage=medium_conf,
            low_confidence_coverage=low_conf,
        )

    def _format_inputs(self, questions: list[str], schema: dict[str, Any]) -> dict[str, str]:
        return {
            "questions": "\n".join(f"{i + 1}. {q}" for i, q in enumerate(questions)),
            "schema": json.dumps(schema, indent=2),
        }

    def evaluate_all(self, questions: list[str], schema: dict[str, Any]) -> dict[str, CoverageAssessment]:
        result = self._build_chain(len(questions)).invoke(self._format_inputs(questions, schema))
        return self._parse_assessments(result, len(questions))

    def evaluate_schema(self, schema: dict[str, Any], questions: list[str]) -> SchemaEvaluation:
        return self._tally(self.evaluate_all(questions, schema))

    async def aevaluate_all(self, questions: list[str], schema: dict[str, Any]) -> dict[str, CoverageAssessment]:
        result = await self._build_chain(len(questions)).ainvoke(self._format_inputs(questions, schema))
        return self._parse_assessments(result, len(questions))

    async def aevaluate_schema(self, schema: dict[str, Any], questions: list[str]) -> SchemaEvaluation:
        return self._tally(await self.aevaluate_all(questions, schema))
