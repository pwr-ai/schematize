from typing import Any

import pytest
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage, HumanMessage
from langchain_core.outputs import ChatGeneration, ChatResult
from langchain_core.runnables import RunnableLambda

from schematize.agents.data_agents import QueryGeneratorAgent
from schematize.agents.output_models import (
    ChatOutput,
    DataAssessmentMergerOutput,
    SchemaAssessmentOutput,
    SchemaGenerationOutput,
    SchemaRefinementOutput,
)
from schematize.agents.schema_generator import SchemaGenerator, SchemaGeneratorPrompts
from schematize.schema.model import NamedFieldDef, SchemaFields
from schematize.utils.load import load_prompts

_USAGE = {"input_tokens": 5, "output_tokens": 3, "total_tokens": 8}

CANNED_SCHEMA = SchemaFields(
    fields=[
        NamedFieldDef(name="party_name", type_="string", description="Name of the party"),
        NamedFieldDef(name="amount", type_="float", description="Monetary amount"),
    ]
)


def _assessment(needs_refinement: bool) -> SchemaAssessmentOutput:
    return SchemaAssessmentOutput(
        overall_score=4.0,
        criteria_scores="{}",
        strengths=["clear"],
        weaknesses=[],
        improvement_suggestions=[],
        is_high_quality=True,
        needs_refinement=needs_refinement,
        assessment_summary="ok",
    )


def _data_merge(needs_refinement: bool) -> DataAssessmentMergerOutput:
    return DataAssessmentMergerOutput(
        summary="ok",
        main_issues=[],
        strengths=["grounded"],
        needs_refinement=needs_refinement,
        confidence="high",
        priority_areas=[],
    )


# Each builder takes the fake's `needs_refinement` flag and returns a valid parsed instance.
_STRUCTURED_BUILDERS = {
    SchemaGenerationOutput: lambda _: SchemaGenerationOutput(is_generated=True, schema_=CANNED_SCHEMA),
    SchemaRefinementOutput: lambda _: SchemaRefinementOutput(is_refined=True, schema_=CANNED_SCHEMA),
    SchemaAssessmentOutput: _assessment,
    DataAssessmentMergerOutput: _data_merge,
    ChatOutput: lambda _: ChatOutput(is_refined=False, end_conversation=True),
    QueryGeneratorAgent.Query: lambda _: QueryGeneratorAgent.Query(query="test query"),
}


class RoutingFakeChatModel(BaseChatModel):
    """Offline stand-in for a chat model shared by every agent.

    Text agents get a canned `AIMessage`; structured-output agents get a valid parsed
    instance routed by the requested output model. `needs_refinement` steers the two
    refinement loops.
    """

    needs_refinement: bool = False
    response_text: str = "canned response"

    @property
    def _llm_type(self) -> str:
        return "routing-fake"

    def _generate(self, messages, stop=None, run_manager=None, **kwargs) -> ChatResult:
        message = AIMessage(content=self.response_text, usage_metadata=_USAGE)
        return ChatResult(generations=[ChatGeneration(message=message)])

    async def _agenerate(self, messages, stop=None, run_manager=None, **kwargs) -> ChatResult:
        return self._generate(messages, stop, run_manager, **kwargs)

    def with_structured_output(self, schema, *, include_raw: bool = False, **kwargs):
        build = _STRUCTURED_BUILDERS[schema]
        needs_refinement = self.needs_refinement

        def _run(_: Any):
            parsed = build(needs_refinement)
            if not include_raw:
                return parsed
            raw = AIMessage(content="", usage_metadata=_USAGE)
            return {"raw": raw, "parsed": parsed, "parsing_error": None}

        return RunnableLambda(_run)


def _stub_feedback(state) -> dict:
    return {"user_feedback": "yes", "messages": [HumanMessage(content="yes")]}


def _stub_human_message(state) -> dict:
    return {
        "messages": [HumanMessage(content="done")],
        "final_messages": [HumanMessage(content="done")],
    }


@pytest.fixture
def fake_llm() -> RoutingFakeChatModel:
    return RoutingFakeChatModel()


@pytest.fixture
def fake_retriever():
    async def retrieve(query: str, max_docs: int = 100) -> list:
        return [{"text": f"document {i} about {query}"} for i in range(5)]

    return retrieve


@pytest.fixture
def prompts() -> SchemaGeneratorPrompts:
    return SchemaGeneratorPrompts(**load_prompts("en", "tax"))


@pytest.fixture
def make_generator(fake_llm, fake_retriever, prompts):
    """Build a `SchemaGenerator` with fakes and the two `input()` nodes stubbed out."""

    def build(llm=None, **overrides) -> SchemaGenerator:
        params = dict(
            min_refinement_rounds=1,
            max_refinement_rounds=2,
            min_data_refinement_rounds=1,
            max_data_refinement_rounds=2,
            data_assessment_num_examples=2,
            data_assessment_top_k=5,
            recursion_limit=50,
        )
        params.update(overrides)
        generator = SchemaGenerator(llm or fake_llm, fake_retriever, prompts, **params)
        generator.human_feedback = _stub_feedback
        generator.human_message = _stub_human_message
        generator.graph = generator.build_graph()
        return generator

    return build
