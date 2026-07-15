"""Regression tests for simulation/LOGGING_ASSESSMENT.md findings."""

import re
import time

import pytest
from loguru import logger

from tests.conftest import RoutingFakeChatModel


@pytest.fixture
def log_sink():
    messages: list[str] = []
    sink_id = logger.add(messages.append, level="DEBUG", format="{message}")
    yield messages
    logger.remove(sink_id)


# --- 1. Aggregate token/cost summary ----------------------------------------------------


def test_stream_graph_updates_logs_token_total(make_generator, log_sink):
    generator = make_generator()
    final_state = generator.stream_graph_updates("Extract parties and amounts from contracts")

    expected_total = sum(u.get("total_tokens", 0) for u in final_state["token_usage"])
    assert expected_total > 0
    assert any(f"total={expected_total}" in m for m in log_sink)


# --- 2. Per-node timing -------------------------------------------------------------------


class _SlowChain:
    def invoke(self, _inputs):
        time.sleep(0.05)
        return "ok"


def test_retrying_chain_logs_elapsed_time(log_sink):
    from schematize.utils.retry import RetryingChain

    chain = RetryingChain(_SlowChain(), max_retries=0, name="SlowThing")
    chain.invoke({})

    assert any(re.search(r"SlowThing.*elapsed.*\d+\.\d+s", m) for m in log_sink)


# --- 3. Repeated loop iterations are distinguishable in the log ---------------------------


def test_repeated_node_passes_are_numbered_in_log(make_generator, log_sink):
    generator = make_generator(min_refinement_rounds=2, max_refinement_rounds=2)
    generator.stream_graph_updates("Extract parties and amounts from contracts")

    assessment_lines = [m for m in log_sink if "SchemaAssessmentAgent" in m and "🤖" in m]
    assert any("pass 1" in m for m in assessment_lines)
    assert any("pass 2" in m for m in assessment_lines)


# --- 4. DEBUG prompt dumps log only interpolated inputs, not static boilerplate -----------


def test_debug_log_skips_static_prompt_boilerplate(log_sink):
    from schematize.agents.basic_agents import ProblemDefinerHelperAgent

    prompt = "STATIC_BOILERPLATE_TEXT_XYZ {user_input}"
    agent = ProblemDefinerHelperAgent(RoutingFakeChatModel(), prompt)
    agent({"user_input": "unique-marker-hello"})

    debug_lines = [m for m in log_sink if "ProblemDefinerHelperAgent" in m]
    assert any("unique-marker-hello" in m for m in debug_lines)
    assert not any("STATIC_BOILERPLATE_TEXT_XYZ" in m for m in debug_lines)


# --- 7. Model/endpoint identity is logged -------------------------------------------------


def test_cli_logs_resolved_model_and_api_url(monkeypatch, tmp_path, fake_llm, fake_retriever):
    import sys
    import types

    from typer.testing import CliRunner

    from schematize._scripts import schema_generator as script

    monkeypatch.setattr(script, "ChatOpenAI", lambda **kwargs: fake_llm)
    stub = types.ModuleType("schematize.retrieval.weaviate")
    stub.WeaviateRetriever = lambda **kwargs: fake_retriever
    monkeypatch.setitem(sys.modules, "schematize.retrieval.weaviate", stub)

    output = tmp_path / "state.json"
    stdin = "Extract parties and amounts from contracts\nyes\ndone\n"

    result = CliRunner().invoke(
        script.app,
        [
            "--model", "gpt-4o-mini",
            "--api-url", "http://example.invalid/v1",
            "--retriever-type", "weaviate",
            "--collection-name", "Contracts",
            "--output", str(output),
            "--min-refinement-rounds", "0",
            "--max-refinement-rounds", "1",
            "--min-data-refinement-rounds", "0",
            "--max-data-refinement-rounds", "1",
            "--data-assessment-num-examples", "2",
            "--data-assessment-top-k", "5",
        ],
        input=stdin,
    )

    assert result.exit_code == 0, result.output
    assert "gpt-4o-mini" in result.output
    assert "http://example.invalid/v1" in result.output


# --- 8. input() prompt has a trailing newline ---------------------------------------------


def test_human_feedback_prompt_ends_with_newline(monkeypatch):
    from schematize.agents.schema_generator import HumanFeedback

    captured = {}

    def fake_input(prompt=""):
        captured["prompt"] = prompt
        return "yes"

    monkeypatch.setattr("builtins.input", fake_input)
    HumanFeedback()({})
    assert captured["prompt"].endswith("\n")


def test_human_message_prompt_ends_with_newline(monkeypatch):
    from schematize.agents.chat_agent import HumanMessageAgent

    captured = {}

    def fake_input(prompt=""):
        captured["prompt"] = prompt
        return "done"

    monkeypatch.setattr("builtins.input", fake_input)
    HumanMessageAgent()({})
    assert captured["prompt"].endswith("\n")
