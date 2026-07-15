"""Regression tests for the fresh-install possible issues."""

import pytest
from openai import AuthenticationError

from schematize.utils.load import load_prompts
from schematize.utils.retry import RetryingChain

# --- 1. Bad API key must not be retried -------------------------------------------------


class _AlwaysAuthFails:
    def __init__(self):
        self.calls = 0

    def invoke(self, _inputs):
        self.calls += 1
        raise AuthenticationError(message="bad key", response=_FakeResponse(), body=None)


class _FakeResponse:
    status_code = 401
    headers = {}
    request = None


def test_authentication_error_is_not_retried():
    fake = _AlwaysAuthFails()
    chain = RetryingChain(fake, max_retries=3)
    with pytest.raises(AuthenticationError):
        chain.invoke({})
    assert fake.calls == 1


# --- 2. EOFError on non-interactive stdin -----------------------------------------------


def test_human_message_agent_eof_raises_clear_error(monkeypatch):
    from schematize.agents.chat_agent import HumanMessageAgent

    monkeypatch.setattr("builtins.input", lambda *a: (_ for _ in ()).throw(EOFError()))
    with pytest.raises(RuntimeError, match="interactive stdin"):
        HumanMessageAgent()({})


def test_human_feedback_eof_raises_clear_error(monkeypatch):
    from schematize.agents.schema_generator import HumanFeedback

    monkeypatch.setattr("builtins.input", lambda *a: (_ for _ in ()).throw(EOFError()))
    with pytest.raises(RuntimeError, match="interactive stdin"):
        HumanFeedback()({})


# --- 4. Malformed WV_PORT ------------------------------------------------------------------


def test_bad_wv_port_raises_clear_error(monkeypatch):
    pytest.importorskip("weaviate")
    monkeypatch.setenv("WV_PORT", "not-a-port")
    from schematize.retrieval.weaviate import WeaviateRetriever

    with pytest.raises(ValueError, match="WV_PORT"):
        WeaviateRetriever(collection_name="X")


# --- 5. Weaviate unreachable ---------------------------------------------------------------


def test_weaviate_unreachable_raises_clear_error():
    pytest.importorskip("weaviate")
    import asyncio

    from schematize.retrieval.weaviate import WeaviateRetriever

    retriever = WeaviateRetriever(collection_name="X", host="127.0.0.1", port=1, grpc_port=2)
    with pytest.raises(ConnectionError, match="127.0.0.1:1"):
        asyncio.run(retriever("q"))


# --- 6. Bad language/system_type ------------------------------------------------------------


def test_load_prompts_bad_language_message():
    with pytest.raises(ValueError, match="xx"):
        load_prompts("xx", "law")


def test_load_prompts_bad_system_type_message():
    with pytest.raises(ValueError, match="xx"):
        load_prompts("en", "xx")


# --- 9. current_schema=None at output time --------------------------------------------------


def test_mocked_script_reports_missing_schema(tmp_path):
    from schematize._scripts.schema_generator_mocked import write_schema

    with pytest.raises(RuntimeError, match="without producing a schema"):
        write_schema(tmp_path / "schema.json", None)
