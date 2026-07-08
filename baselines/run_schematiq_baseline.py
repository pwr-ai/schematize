"""Run ScheMatiQ (https://github.com/shaharl6000/ScheMatiQ) as a baseline for one case.

Retrieves documents from the HF corpus, runs ScheMatiQ schema discovery with the
case dialogue as query, and writes a schematize-compatible ``state.json`` so
``scripts/evaluate_schema.py`` can score it unchanged.

Usage:
    uv run python baselines/run_schematiq_baseline.py --case pl_age --model gpt-5.4-mini
"""

import asyncio
import json
import logging
import os
import time
from pathlib import Path
from typing import Annotated, Any, Optional

import typer
import yaml
from dotenv import load_dotenv

app = typer.Typer(add_completion=False)

REPO_ROOT = Path(__file__).parent.parent
_DEFAULT_CASES = REPO_ROOT / "data/cases"
_DEFAULT_OUTPUT = REPO_ROOT / "outputs/schematiq"

load_dotenv()
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def _load_case(cases_path: Path, case_name: str) -> dict:
    case_file = cases_path / f"{case_name}.yaml"
    if not case_file.exists():
        available = [p.stem for p in cases_path.glob("*.yaml")]
        raise typer.BadParameter(f"Case '{case_name}' not found. Available: {available}")
    return yaml.safe_load(case_file.read_text())


def build_query(case: dict, full_dialogue: bool) -> str:
    if not full_dialogue:
        return case["user_input"]
    parts = [case["user_input"]]
    if case.get("problem_help") and case.get("user_feedback"):
        parts.append("Pytania doprecyzowujące:\n" + case["problem_help"].strip())
        parts.append("Odpowiedzi użytkownika:\n" + case["user_feedback"].strip())
    return "\n\n".join(parts)


def columns_to_schema_fields(schema) -> dict[str, Any]:
    """Convert ScheMatiQ Schema columns to schematize SchemaFields dict."""
    fields = []
    for col in schema.columns:
        description = col.definition or ""
        if col.rationale:
            description = f"{description} {col.rationale}".strip()
        field = {"name": col.name, "description": description}
        if col.allowed_values:
            field |= {"type_": "enum", "enum_name": col.name, "enum_values": list(col.allowed_values)}
        else:
            field |= {"type_": "string", "enum_name": None, "enum_values": []}
        fields.append(field)
    return {"fields": fields}


@app.command()
def main(
    case: Annotated[str, typer.Option("--case", help="Case name (stem of YAML file in cases-path)")],
    model: Annotated[str, typer.Option("--model", help="LLM model name")] = "gpt-5.4-mini",
    cases_path: Annotated[Path, typer.Option("--cases-path")] = _DEFAULT_CASES,
    output: Annotated[Path, typer.Option("--output", help="Output root directory")] = _DEFAULT_OUTPUT,
    dataset: Annotated[str, typer.Option()] = "JuDDGES/pl-court-raw",
    text_column: Annotated[str, typer.Option()] = "full_text",
    max_documents: Annotated[Optional[int], typer.Option(help="Corpus cap for the FAISS index (None = full corpus)")] = None,
    top_k_docs: Annotated[int, typer.Option(help="Documents fed to ScheMatiQ")] = 50,
    max_keys_schema: Annotated[Optional[int], typer.Option(help="Column cap (None = unlimited)")] = None,
    documents_batch_size: Annotated[int, typer.Option()] = 4,
    max_iters: Annotated[int, typer.Option()] = 6,
    temperature: Annotated[float, typer.Option()] = 1,
    passage_k: Annotated[int, typer.Option(help="Passages per document")] = 15,
    device: Annotated[Optional[str], typer.Option()] = None,
    full_dialogue: Annotated[bool, typer.Option(help="Give ScheMatiQ the full case dialogue as query")] = True,
    api_key: Annotated[Optional[str], typer.Option("--api-key", envvar="API_KEY")] = None,
    api_url: Annotated[Optional[str], typer.Option("--api-url", envvar="API_URL")] = None,
) -> None:
    if api_key:
        os.environ["OPENAI_API_KEY"] = api_key
    if api_url:
        os.environ["OPENAI_BASE_URL"] = api_url

    from schematiq.core.llm_backends import OpenAILLM
    from schematiq.core.retrievers import EmbeddingRetriever
    from schematiq.core.schematiq import discover_schema, save_schema

    from schematize.retrieval.huggingface import MMLWRobertaV2Retriever

    class PatchedOpenAILLM(OpenAILLM):
        """ScheMatiQ passes ``max_output_tokens`` to all backends, but its OpenAI
        path forwards kwargs verbatim to chat.completions.create(), which only
        accepts ``max_tokens``. Additionally, the native OpenAI API (unlike a
        LiteLLM proxy) rejects ``max_tokens``/non-default ``temperature`` for
        reasoning models — on such errors, retry with the adjusted params."""

        def generate(self, prompt, **kwargs):
            if "max_output_tokens" in kwargs:
                kwargs["max_tokens"] = kwargs.pop("max_output_tokens")
            try:
                return super().generate(prompt, **kwargs)
            except Exception as e:
                msg = str(e)
                retried = False
                if "max_completion_tokens" in msg and "max_tokens" in msg:
                    tokens = kwargs.pop("max_tokens", None) or self._default_args.get("max_tokens")
                    self._default_args.pop("max_tokens", None)
                    self._default_args["max_completion_tokens"] = tokens
                    retried = True
                if "temperature" in msg and ("unsupported" in msg.lower() or "does not support" in msg.lower()):
                    kwargs.pop("temperature", None)
                    self._default_args.pop("temperature", None)
                    retried = True
                if not retried:
                    raise
                return super().generate(prompt, **kwargs)

    case_data = _load_case(cases_path, case)
    variant = "full_dialogue" if full_dialogue else "query_only"
    gen_name = f"schematiq_{model}_{variant}"
    out_dir = output / gen_name / case
    if (out_dir / "state.json").exists():
        typer.echo(f"Skipping {case} (state.json exists)")
        raise typer.Exit()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Same document retriever as schematize's default (config/retriever/mmlw.yaml) so the
    # baseline builds its document shortlist with the same model as the schematize pipeline.
    doc_retriever = MMLWRobertaV2Retriever(
        dataset_name=dataset,
        text_column=text_column,
        max_documents=max_documents,
        device=device,
    )
    # Localize ScheMatiQ's passage retriever to mmlw for Polish (its default is a weak
    # multilingual MiniLM). Algorithm unchanged; only the embedding backbone is swapped.
    passage_embedding_model = "sdadas/mmlw-retrieval-roberta-large-v2"
    llm = PatchedOpenAILLM(model=model, temperature=temperature)

    token_usage: list[dict] = []
    _orig_create = llm._client.chat.completions.create

    def _create_with_usage_tracking(*args, **kwargs):
        resp = _orig_create(*args, **kwargs)
        if resp.usage:
            cached_tokens = getattr(resp.usage.prompt_tokens_details, "cached_tokens", None) or 0
            token_usage.append({
                "node": "ScheMatiQ",
                "input_tokens": resp.usage.prompt_tokens,
                "output_tokens": resp.usage.completion_tokens,
                "total_tokens": resp.usage.total_tokens,
                "input_token_details": {"cache_read": cached_tokens},
            })
        return resp

    llm._client.chat.completions.create = _create_with_usage_tracking

    passage_retriever = EmbeddingRetriever(
        model_name=passage_embedding_model, k=passage_k, device=device, enable_preprocessing=False
    )

    query = build_query(case_data, full_dialogue)

    typer.echo(f"=== {case}: retrieving {top_k_docs} documents ===")
    results = asyncio.run(doc_retriever(query, max_docs=top_k_docs))
    documents = [r[text_column] or "" for r in results]
    filenames = [str(r.get("judgment_id") or r.get("_id") or f"doc_{i}") for i, r in enumerate(results)]

    typer.echo(f"=== {case}: running ScheMatiQ schema discovery ===")
    start = time.time()
    schema, contributing, non_contributing, evolution = discover_schema(
        query=query,
        documents=documents,
        filenames=filenames,
        max_keys_schema=max_keys_schema,
        llm=llm,
        retriever=passage_retriever,
        documents_batch_size=documents_batch_size,
        context_window_size=llm.context_window_size,
        max_iters=max_iters,
    )
    elapsed = time.time() - start
    typer.echo(f"{case}: {len(schema)} columns in {elapsed:.0f}s")

    save_schema(
        out_dir / "schematiq_artifact.json",
        query=query,
        retriever_cfg={
            "doc_retriever": "sdadas/mmlw-retrieval-roberta-large-v2",
            "passage_retriever": passage_embedding_model,
            "k": passage_k,
        },
        backend_cfg={"provider": "openai", "model": model, "temperature": temperature},
        docs_path=f"{dataset} (top {top_k_docs} by mmlw retrieval, corpus cap {max_documents})",
        schema=schema,
        contributing_files=contributing,
        non_contributing_files=non_contributing,
        schema_evolution=evolution,
    )

    schema_dict = columns_to_schema_fields(schema)
    state_path = out_dir / "state.json"
    state_path.write_text(
        json.dumps(
            {
                "current_schema": schema_dict,
                "schema_history": [schema_dict],
                "token_usage": token_usage,
                "baseline": {"system": "ScheMatiQ", "variant": variant, "model": model, "elapsed_seconds": elapsed},
            },
            indent=2,
            ensure_ascii=False,
        )
    )
    typer.echo(f"Saved {state_path}")


if __name__ == "__main__":
    app()
