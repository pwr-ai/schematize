"""Collect ScheMatiQ baseline states + evaluations and upload as a private HF dataset.

Builds two configs:
- ``schemas``: one row per (case, run) with the generated schema and metadata.
- ``evaluation``: one row per (case, run, schema_index, expert) with coverage metrics.

Usage:
    HF_TOKEN=... uv run python baselines/upload_baseline_results.py \
        --generation-name schematiq_gpt-5.4-mini_full_dialogue \
        --repo-id ktagowski/schematize-schematiq-baseline
"""

import json
import os
from pathlib import Path
from typing import Annotated

import typer
from datasets import Dataset

app = typer.Typer()

REPO_ROOT = Path(__file__).parent.parent


@app.command()
def main(
    generation_name: Annotated[str, typer.Option()] = "schematiq_gpt-5.4-mini_full_dialogue",
    eval_model: Annotated[str, typer.Option()] = "gpt-5.4-mini",
    state_root: Annotated[Path, typer.Option()] = REPO_ROOT / "multirun/generated_schemas",
    eval_root: Annotated[Path, typer.Option()] = REPO_ROOT / "outputs/evaluation",
    repo_id: Annotated[str, typer.Option()] = "ktagowski/schematize-schematiq-baseline",
) -> None:
    token = os.environ.get("HF_TOKEN")
    if not token:
        raise typer.Exit("HF_TOKEN not set")

    schema_rows = []
    eval_rows = []

    for state_path in sorted((state_root / generation_name).glob("*/*/state.json")):
        run_name = state_path.parent.name
        case_name = state_path.parent.parent.name
        state = json.loads(state_path.read_text())
        baseline_meta = state.get("baseline", {})
        artifact_path = state_path.parent / "schematiq_artifact.json"
        artifact = json.loads(artifact_path.read_text()) if artifact_path.exists() else {}

        schema_rows.append(
            {
                "case_name": case_name,
                "run_name": run_name,
                "system": baseline_meta.get("system", "ScheMatiQ"),
                "variant": baseline_meta.get("variant"),
                "generation_model": baseline_meta.get("model"),
                "user_input": state.get("user_input"),
                "query": state.get("query"),
                "num_fields": len(state["current_schema"]["fields"]),
                "schema_json": json.dumps(state["current_schema"], ensure_ascii=False),
                "schematiq_artifact_json": json.dumps(artifact, ensure_ascii=False),
                "elapsed_seconds": baseline_meta.get("elapsed_seconds"),
            }
        )

        eval_path = (
            eval_root / eval_model / generation_name
            / state_path.relative_to(state_root / generation_name).parent / "evaluation.json"
        )
        # evaluate_schema.py writes evaluation.json next to the hydra output dir
        # mirroring the state layout; fall back to the state dir itself.
        if not eval_path.exists():
            eval_path = state_path.parent / "evaluation.json"
        if not eval_path.exists():
            typer.echo(f"WARNING: no evaluation.json for {case_name}/{run_name}")
            continue

        evaluation = json.loads(eval_path.read_text())
        for schema_eval in evaluation.get("evaluations", []):
            for expert in schema_eval.get("experts", []):
                eval_rows.append(
                    {
                        "case_name": case_name,
                        "run_name": run_name,
                        "system": baseline_meta.get("system", "ScheMatiQ"),
                        "variant": baseline_meta.get("variant"),
                        "generation_model": baseline_meta.get("model"),
                        "evaluation_model": eval_model,
                        "schema_index": schema_eval["schema_index"],
                        "num_fields": schema_eval["num_fields"],
                        "expert": expert["expert"],
                        "total_questions": expert["total_questions"],
                        "covered_questions": expert["covered_questions"],
                        "high_confidence": expert["high_confidence"],
                        "medium_confidence": expert["medium_confidence"],
                        "low_confidence": expert["low_confidence"],
                        "coverage_rate": expert["covered_questions"] / expert["total_questions"]
                        if expert["total_questions"] else 0.0,
                    }
                )

    if not schema_rows:
        raise typer.Exit(f"No states found under {state_root / generation_name}")

    typer.echo(f"{len(schema_rows)} schema rows, {len(eval_rows)} evaluation rows → {repo_id}")

    Dataset.from_list(schema_rows).push_to_hub(
        repo_id, config_name="schemas", private=True, token=token
    )
    if eval_rows:
        Dataset.from_list(eval_rows).push_to_hub(
            repo_id, config_name="evaluation", private=True, token=token
        )
    typer.echo(f"Uploaded to https://huggingface.co/datasets/{repo_id} (private)")


if __name__ == "__main__":
    app()
