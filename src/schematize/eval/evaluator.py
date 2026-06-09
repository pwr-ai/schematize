import json
from dataclasses import dataclass
from typing import Any, Literal

from langchain_core.language_models import BaseChatModel
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field


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


class SchemaEvaluator:
    def __init__(self, llm: BaseChatModel, evaluation_prompt: str):
        self.llm = llm
        self.evaluation_prompt_template = PromptTemplate.from_template(evaluation_prompt)

    def evaluate_question(self, question: str, schema: dict[str, Any]) -> CoverageAssessment:
        schema_json = json.dumps(schema, indent=2)
        structured_llm = self.llm.with_structured_output(CoverageAssessment)
        chain = self.evaluation_prompt_template | structured_llm
        return chain.invoke({"question": question, "schema": schema_json})

    def evaluate_schema(self, schema: dict[str, Any], questions: list[str]) -> SchemaEvaluation:
        covered_count = 0
        high_conf = 0
        medium_conf = 0
        low_conf = 0

        for question in questions:
            evaluation = self.evaluate_question(question, schema)
            if evaluation.is_covered:
                covered_count += 1
                if evaluation.confidence == "high":
                    high_conf += 1
                elif evaluation.confidence == "medium":
                    medium_conf += 1
                elif evaluation.confidence == "low":
                    low_conf += 1

        return SchemaEvaluation(
            total_questions=len(questions),
            covered_questions=covered_count,
            high_confidence_coverage=high_conf,
            medium_confidence_coverage=medium_conf,
            low_confidence_coverage=low_conf,
        )
