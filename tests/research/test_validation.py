"""Offline validation for paper-reproduction assets."""

import ast
import os
import subprocess
import sys
from pathlib import Path

import nbformat
import pytest
import yaml

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research"


def _run(*args: str) -> subprocess.CompletedProcess[str]:
    env = os.environ | {"PYTHONPATH": str(ROOT / "src")}
    return subprocess.run(
        [sys.executable, *args],
        cwd=ROOT,
        env=env,
        text=True,
        capture_output=True,
        check=False,
    )


@pytest.mark.parametrize("path", sorted(RESEARCH.rglob("*.yaml")))
def test_research_yaml_is_valid(path: Path) -> None:
    assert yaml.safe_load(path.read_text(encoding="utf-8")) is not None


@pytest.mark.parametrize("path", sorted(RESEARCH.rglob("*.sh")))
def test_research_shell_scripts_parse(path: Path) -> None:
    result = subprocess.run(["bash", "-n", str(path)], text=True, capture_output=True, check=False)
    assert result.returncode == 0, result.stderr


@pytest.mark.parametrize(
    "path",
    [
        *sorted((RESEARCH / "scripts" / "experiments").glob("*.sh")),
        RESEARCH / "scripts" / "schematiq" / "baseline_schematiq.sh",
        RESEARCH / "scripts" / "schematiq" / "eval_schematiq.sh",
    ],
)
def test_experiment_runners_cover_every_paper_case(path: Path) -> None:
    assert "CASES=(pl_age pl_personal_rights pl_medical_errors)" in path.read_text(encoding="utf-8")


PAPER_MODELS = (
    "claude-sonnet-4.6",
    "gpt-5.4-nano",
    "gpt-5.4-mini",
    "gpt-5.4",
    "llama-4-scout-17b",
    "qwen3.6-35b-a3b",
    "gemma-4-e4b-it",
)


@pytest.mark.parametrize(
    "path",
    [
        RESEARCH / "scripts" / "experiments" / "final_run.sh",
        RESEARCH / "scripts" / "experiments" / "ablation.sh",
        RESEARCH / "scripts" / "experiments" / "eval_ablation.sh",
        RESEARCH / "scripts" / "experiments" / "baseline.sh",
        RESEARCH / "scripts" / "experiments" / "baseline_no_pd.sh",
        RESEARCH / "scripts" / "experiments" / "eval_baseline.sh",
        RESEARCH / "scripts" / "experiments" / "eval_baseline_no_pd.sh",
        RESEARCH / "scripts" / "experiments" / "eval_single_run.sh",
        RESEARCH / "scripts" / "schematiq" / "baseline_schematiq.sh",
        RESEARCH / "scripts" / "schematiq" / "eval_schematiq.sh",
    ],
)
def test_model_runners_cover_every_paper_model(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for model in PAPER_MODELS:
        assert model in text


@pytest.mark.parametrize(
    "path",
    [
        RESEARCH / "scripts" / "experiments" / "search_params.sh",
        RESEARCH / "scripts" / "experiments" / "eval_multirun.sh",
    ],
)
def test_parameter_search_scripts_use_paper_generation_model(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    assert "gpt-5.4-nano" in text
    assert "claude-sonnet-4.6" not in text


@pytest.mark.parametrize("path", sorted((RESEARCH / "notebooks").glob("*.ipynb")))
def test_research_notebooks_are_clean_and_parse(path: Path) -> None:
    notebook = nbformat.read(path, as_version=4)
    for cell in notebook.cells:
        assert not cell.get("outputs"), f"{path} contains committed cell output"
        if cell.cell_type != "code" or "%" in cell.source or "!" in cell.source:
            continue
        ast.parse(cell.source)


@pytest.mark.parametrize(
    ("script", "arguments"),
    [
        ("schema_generator_mocked.py", ["case=pl_age", "model_name=placeholder", "validate_only=true"]),
        ("schema_generator_ablation.py", ["case=pl_age", "model_name=placeholder", "validate_only=true"]),
        (
            "evaluate_schema.py",
            ["case_name=pl_age", "state_dir=.", "generation_model_name=placeholder", "validate_only=true"],
        ),
        ("evaluate_annotator_agreement.py", ["case_name=pl_age", "validate_only=true"]),
    ],
)
def test_hydra_runners_validate_without_network(script: str, arguments: list[str]) -> None:
    result = _run(str(RESEARCH / "scripts" / script), *arguments)
    assert result.returncode == 0, result.stderr
    assert "Validated" in result.stdout + result.stderr


@pytest.mark.parametrize(
    ("script", "arguments"),
    [
        ("baseline.py", ["--case", "pl_age", "--model", "placeholder", "--validate-only"]),
        (
            "schematiq/run_schematiq_baseline.py",
            ["--case", "pl_age", "--model", "placeholder", "--validate-only"],
        ),
    ],
)
def test_typer_research_runners_validate_without_network(script: str, arguments: list[str]) -> None:
    result = _run(str(RESEARCH / "scripts" / script), *arguments)
    assert result.returncode == 0, result.stderr
    assert "Validated" in result.stdout + result.stderr
