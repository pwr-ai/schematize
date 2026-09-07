import importlib.util
import json
import sys
import types
from pathlib import Path

import pytest
from typer.testing import CliRunner


def test_interactive_script_runs_end_to_end(monkeypatch, tmp_path, fake_llm, fake_retriever):
    from schematize._scripts import schema_generator as script

    monkeypatch.setattr(script, "ChatOpenAI", lambda **kwargs: fake_llm)
    # The weaviate extra isn't installed in CI; stub the module so the retriever import resolves.
    stub = types.ModuleType("schematize.retrieval.weaviate")
    stub.WeaviateRetriever = lambda **kwargs: fake_retriever
    monkeypatch.setitem(sys.modules, "schematize.retrieval.weaviate", stub)

    output = tmp_path / "state.json"
    # Three lines feed: problem description, HumanFeedback, HumanMessageAgent.
    stdin = "Extract parties and amounts from contracts\nyes\ndone\n"

    result = CliRunner().invoke(
        script.app,
        [
            "--model", "gpt-4o-mini",
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
    assert output.exists()
    state = json.loads(output.read_text())
    assert state["current_schema"]["fields"]
    assert state["end_conversation"] is True


# The mocked research runner needs the [research] extra; skip cleanly when absent.
pytest.importorskip("hydra")

_ROOT = Path(__file__).resolve().parents[1]


def _load_research_script(name: str):
    path = _ROOT / "research" / "scripts" / name
    spec = importlib.util.spec_from_file_location(name.removesuffix(".py"), path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def test_load_cases(tmp_path):
    load_cases = _load_research_script("schema_generator_mocked.py").load_cases

    (tmp_path / "sample.yaml").write_text("user_input: hello\nhuman_message: bye\n")
    cases = load_cases(tmp_path)

    assert cases == {"sample": {"user_input": "hello", "human_message": "bye"}}


def test_mock_node_factories():
    script = _load_research_script("schema_generator_mocked.py")
    create_mock_human_message = script.create_mock_human_message
    create_mock_problem_helper = script.create_mock_problem_helper
    create_mock_user_feedback = script.create_mock_user_feedback

    helper = create_mock_problem_helper("help text")({})
    assert helper["problem_help"] == "help text"
    assert helper["messages"][0].content == "help text"

    feedback = create_mock_user_feedback("feedback text")({})
    assert feedback["user_feedback"] == "feedback text"

    message = create_mock_human_message("a message")({})
    assert message["messages"][0].content == "a message"
    assert message["final_messages"][0].content == "a message"
