"""Run ScheMatiQ (https://github.com/shaharl6000/ScheMatiQ) as a baseline on data/cases.

For each case:
1. Retrieve top-K documents from the HF corpus (JuDDGES/pl-court-raw) using the
   case's user_input as query (multilingual MiniLM + FAISS, capped corpus).
2. Run ScheMatiQ schema discovery with the full case dialogue as the query.
3. Save the ScheMatiQ artifact and a schematize-compatible ``state.json``
   (``current_schema`` in SchemaFields format) so ``evaluate_schema.py`` can
   score it against the expert questions unchanged.

Usage:
    uv run python baselines/run_schematiq_baseline.py --model gpt-5.4-mini
"""

import asyncio
import json
import logging
import time
from pathlib import Path
from typing import Annotated, Any, Optional

import typer
import yaml
from dotenv import load_dotenv

app = typer.Typer()

REPO_ROOT = Path(__file__).parent.parent


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
        if col.allowed_values:
            field = {
                "name": col.name,
                "type_": "enum",
                "enum_name": col.name,
                "enum_values": list(col.allowed_values),
                "description": description,
            }
        else:
            field = {
                "name": col.name,
                "type_": "string",
                "enum_name": None,
                "enum_values": [],
                "description": description,
            }
        fields.append(field)
    return {"fields": fields}


@app.command()
def main(
    model: Annotated[str, typer.Option()] = "gpt-5.4-mini",
    cases_dir: Annotated[Path, typer.Option()] = REPO_ROOT / "data/cases",
    output_root: Annotated[Path, typer.Option()] = REPO_ROOT / "multirun/generated_schemas",
    dataset: Annotated[str, typer.Option()] = "JuDDGES/pl-court-raw",
    text_column: Annotated[str, typer.Option()] = "full_text",
    max_documents: Annotated[Optional[int], typer.Option(help="Corpus cap for the FAISS index (None = full corpus)")] = None,
    top_k_docs: Annotated[int, typer.Option(help="Documents fed to ScheMatiQ")] = 50,
    max_keys_schema: Annotated[Optional[int], typer.Option(help="Column cap (None = unlimited, ScheMatiQ's native default)")] = None,
    documents_batch_size: Annotated[int, typer.Option()] = 4,
    max_iters: Annotated[int, typer.Option()] = 6,
    temperature: Annotated[float, typer.Option()] = 0.2,
    passage_k: Annotated[int, typer.Option(help="Passages per document (ScheMatiQ retriever)")] = 8,
    device: Annotated[Optional[str], typer.Option(help="Torch device for embedding models (None = auto-detect)")] = None,
    full_dialogue: Annotated[bool, typer.Option(help="Give ScheMatiQ the full case dialogue as query")] = True,
    run_name: Annotated[str, typer.Option()] = "run_0",
) -> None:
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    load_dotenv(".env")

    from schematiq.core.llm_backends import OpenAILLM
    from schematiq.core.retrievers import EmbeddingRetriever
    from schematiq.core.schematiq import discover_schema, save_schema

    class PatchedOpenAILLM(OpenAILLM):
        """ScheMatiQ passes ``max_output_tokens`` to all backends, but its OpenAI
        path forwards kwargs verbatim to chat.completions.create(), which only
        accepts ``max_tokens``. Additionally, the native OpenAI API (unlike the
        LiteLLM proxy) rejects ``max_tokens`` and non-default ``temperature`` for
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

    from schematize.retrieval.huggingface import MMLWRobertaV2Retriever

    # Same document retriever as schematize's default (config/retriever/mmlw.yaml) so the
    # baseline builds its document shortlist with the same model as the schematize pipeline.
    doc_retriever = MMLWRobertaV2Retriever(
        dataset_name=dataset,
        text_column=text_column,
        max_documents=max_documents,
        device=device,
        index_path=REPO_ROOT / ".cache/schematize" / f"{dataset.replace('/', '_')}_mmlw_{max_documents or 'full'}",
    )
    # Localize ScheMatiQ's passage retriever to mmlw for Polish (its default is a weak
    # multilingual MiniLM). Algorithm unchanged; only the embedding backbone is swapped.
    passage_embedding_model = "sdadas/mmlw-retrieval-roberta-large-v2"

    llm = PatchedOpenAILLM(model=model, temperature=temperature)
    passage_retriever = EmbeddingRetriever(
        model_name=passage_embedding_model,
        k=passage_k,
        device=device,
        enable_preprocessing=False,  # preprocessor targets academic papers, not court rulings
    )

    variant = "full_dialogue" if full_dialogue else "query_only"
    gen_name = f"schematiq_{model}_{variant}"

    for case_path in sorted(cases_dir.glob("*.yaml")):
        case = yaml.safe_load(case_path.read_text())
        case_name = case_path.stem
        out_dir = output_root / gen_name / case_name / run_name
        if (out_dir / "state.json").exists():
            typer.echo(f"Skipping {case_name} (state.json exists)")
            continue
        out_dir.mkdir(parents=True, exist_ok=True)

        # One query drives both document selection and schema discovery, so the
        # retrieved documents match what ScheMatiQ actually reasons over.
        schema_query = build_query(case, full_dialogue)
        retrieval_query = schema_query

        typer.echo(f"=== {case_name}: retrieving {top_k_docs} documents ===")
        results = asyncio.run(doc_retriever(retrieval_query, max_docs=top_k_docs))
        documents = [r[text_column] or "" for r in results]
        filenames = [str(r.get("judgment_id") or r.get("_id") or f"doc_{i}") for i, r in enumerate(results)]

        typer.echo(f"=== {case_name}: running ScheMatiQ schema discovery ===")
        start = time.time()
        schema, contributing, non_contributing, evolution = discover_schema(
            query=schema_query,
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
        typer.echo(f"{case_name}: {len(schema)} columns in {elapsed:.0f}s")

        save_schema(
            out_dir / "schematiq_artifact.json",
            query=schema_query,
            retriever_cfg={
                "doc_retriever": "sdadas/mmlw-retrieval-roberta-large-v2",
                "passage_retriever": passage_embedding_model,
                "k": passage_k,
            },
            backend_cfg={"provider": "openai", "model": model, "temperature": temperature},
            docs_path=f"{dataset} (top {top_k_docs} by MiniLM retrieval, corpus cap {max_documents})",
            schema=schema,
            contributing_files=contributing,
            non_contributing_files=non_contributing,
            schema_evolution=evolution,
        )

        state = {
            "user_input": case["user_input"],
            "problem_help": case.get("problem_help"),
            "user_feedback": case.get("user_feedback"),
            "query": retrieval_query,
            "schema_query": schema_query,
            "current_schema": columns_to_schema_fields(schema),
            "schema_history": [],
            "baseline": {
                "system": "ScheMatiQ",
                "variant": variant,
                "model": model,
                "elapsed_seconds": elapsed,
            },
        }
        (out_dir / "state.json").write_text(json.dumps(state, indent=2, ensure_ascii=False))
        typer.echo(f"Saved {out_dir / 'state.json'}")


if __name__ == "__main__":
    app()
