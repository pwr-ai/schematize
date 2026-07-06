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


@dataclass
class AgreementEvaluation:
    """Aggregate agreement result for one annotator's questions against another's.

    Attributes:
        total_questions: Number of target questions evaluated.
        covered_questions: Target questions already asked by the reference annotator (any confidence).
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


def _count_coverage(assessments: dict[str, CoverageAssessment]) -> tuple[int, int, int, int, int]:
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
    return len(assessments), covered_count, high_conf, medium_conf, low_conf


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
        return SchemaEvaluation(*_count_coverage(assessments))

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


class AnnotatorAgreementEvaluator:
    """Scores how well one annotator's questions are covered by another's.

    For each target question the LLM judge checks whether an equivalent or more
    general question already exists in the reference list, reporting a
    `CoverageAssessment` with a confidence level. The aggregate result is an
    `AgreementEvaluation`. The relation is not symmetric: evaluating A against B
    answers "how many of A's questions does B already ask", which differs from
    evaluating B against A.

    Args:
        llm: Language model used as the judge.
        agreement_prompt: Prompt template with `{target_questions}` and
            `{reference_questions}` placeholders.
        max_retries: Retries for structured-output calls that fail with an
            `openai.OpenAIError`. Default: 3.
    """

    def __init__(
        self,
        llm: BaseChatModel,
        agreement_prompt: str,
        max_retries: int = 3,
    ):
        self.llm = llm
        self.agreement_prompt_template = PromptTemplate.from_template(agreement_prompt)
        self.max_retries = max_retries

    def _build_chain(self, n: int) -> StructuredOutputRunner:
        return StructuredOutputRunner(
            self.llm,
            _build_batch_model(n),
            self.agreement_prompt_template,
            self.max_retries,
            include_raw=False,
        )

    def _parse_assessments(self, result: Any, n: int) -> dict[str, CoverageAssessment]:
        return {f"question_{i + 1}": getattr(result, f"question_{i + 1}") for i in range(n)}

    def _tally(self, assessments: dict[str, CoverageAssessment]) -> AgreementEvaluation:
        return AgreementEvaluation(*_count_coverage(assessments))

    def _format_inputs(self, target_questions: list[str], reference_questions: list[str]) -> dict[str, str]:
        return {
            "target_questions": "\n".join(f"{i + 1}. {q}" for i, q in enumerate(target_questions)),
            "reference_questions": "\n".join(f"{i + 1}. {q}" for i, q in enumerate(reference_questions)),
        }

    def evaluate_all(
        self, target_questions: list[str], reference_questions: list[str]
    ) -> dict[str, CoverageAssessment]:
        result = self._build_chain(len(target_questions)).invoke(
            self._format_inputs(target_questions, reference_questions)
        )
        return self._parse_assessments(result, len(target_questions))

    def evaluate_agreement(self, target_questions: list[str], reference_questions: list[str]) -> AgreementEvaluation:
        return self._tally(self.evaluate_all(target_questions, reference_questions))

    async def aevaluate_all(
        self, target_questions: list[str], reference_questions: list[str]
    ) -> dict[str, CoverageAssessment]:
        result = await self._build_chain(len(target_questions)).ainvoke(
            self._format_inputs(target_questions, reference_questions)
        )
        return self._parse_assessments(result, len(target_questions))

    async def aevaluate_agreement(
        self, target_questions: list[str], reference_questions: list[str]
    ) -> AgreementEvaluation:
        return self._tally(await self.aevaluate_all(target_questions, reference_questions))
