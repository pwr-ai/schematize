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

    def evaluate_all(self, questions: list[str], schema: dict[str, Any]) -> dict[str, CoverageAssessment]:
        schema_json = json.dumps(schema, indent=2)
        numbered = "\n".join(f"{i + 1}. {q}" for i, q in enumerate(questions))
        batch_model = _build_batch_model(len(questions))
        structured_llm = self.llm.with_structured_output(batch_model)
        chain = self.evaluation_prompt_template | structured_llm
        result = chain.invoke({"questions": numbered, "schema": schema_json})
        return {f"question_{i + 1}": getattr(result, f"question_{i + 1}") for i in range(len(questions))}

    def evaluate_schema(self, schema: dict[str, Any], questions: list[str]) -> SchemaEvaluation:
        assessments = self.evaluate_all(questions, schema)
        covered_count = 0
        high_conf = 0
        medium_conf = 0
        low_conf = 0

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
            total_questions=len(questions),
            covered_questions=covered_count,
            high_confidence_coverage=high_conf,
            medium_confidence_coverage=medium_conf,
            low_confidence_coverage=low_conf,
        )
