import json
from dataclasses import dataclass
from typing import Any, Literal

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field, create_model

from schematize.utils.retry import StructuredOutputRunner


class CoverageAssessment(BaseModel):
    """Per-question verdict from the LLM judge.

    Attributes:
        is_covered: Whether the schema contains the fields needed to answer the question.
        confidence: How certain the judge is — `high` (clearly covered or not), `medium`
            (partially covered or ambiguous), `low` (uncertain).
    """

    is_covered: bool = Field(description="Whether the question is covered by the schema")
    confidence: Literal["high", "medium", "low"] = Field(
        description="Confidence level: high (clearly covered/not covered), medium (partially covered or unclear), low (uncertain)"
    )


@dataclass
class SchemaEvaluation:
    """Aggregate evaluation result for a schema against a question set.

    Attributes:
        total_questions: Number of questions evaluated.
        covered_questions: Questions answered by the schema (any confidence).
        high_confidence_coverage: Covered questions judged with high confidence.
        medium_confidence_coverage: Covered questions judged with medium confidence.
        low_confidence_coverage: Covered questions judged with low confidence.
    """

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
    """Scores an extraction schema against a set of expert questions.

    For each question the LLM judge checks whether the schema contains the fields
    needed to answer it, and reports a `CoverageAssessment` with a confidence level.
    The aggregate result is a `SchemaEvaluation` with confidence-weighted counts.

    Args:
        llm: Language model used as the judge.
        evaluation_prompt: Prompt template with `{questions}` and `{schema}` placeholders.
        max_retries: Retries for structured-output calls that fail with an
            `openai.OpenAIError`. Default: 3.
    """

    def __init__(
        self,
        llm: BaseChatModel,
        evaluation_prompt: str,
        max_retries: int = 3,
    ):
        self.llm = llm
        self.evaluation_prompt_template = PromptTemplate.from_template(evaluation_prompt)
        self.max_retries = max_retries

    def _build_chain(self, n: int) -> StructuredOutputRunner:
        return StructuredOutputRunner(
            self.llm,
            _build_batch_model(n),
            self.evaluation_prompt_template,
            self.max_retries,
            include_raw=False,
        )

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
