# Research reproduction

This directory contains the data, runners, configuration, and analyses used for
the Schematize paper. It is not part of the installed library's stable API.

## Contents

- `data/cases/`: fixed problem-definition dialogues used to generate schemas.
- `data/eval/`: expert-authored question sets used for coverage evaluation.
- `config/`: Hydra configurations for generation, ablation, and evaluation.
- `scripts/`: reproduction runners, baselines, and the ScheMatiQ adapter.
- `notebooks/`: analyses that regenerate paper figures and tables from outputs.

The study uses the `pl/law` prompt set, the `JuDDGES/pl-court-raw` Hugging Face
dataset, and `MMLWRobertaV2Retriever`. Its primary configuration uses two to
three criteria-refinement rounds, two to four data-grounded rounds, and one
document per data-grounded round.

## Setup

```bash
uv sync --extra dev --extra research --extra huggingface
```

Set `API_KEY` and optionally `API_URL` in `.env`. The experiments write
generated results to the gitignored `outputs/` and `multirun/` directories.

## Reproduction workflow

1. Search for the best hyperparameter configuration with
   `research/scripts/experiments/search_params.sh`.
2. Generate full-system schemas with `research/scripts/experiments/final_run.sh`.
3. Run the baseline and ablation scripts under `research/scripts/experiments/`.
4. Evaluate the generated states with the corresponding `eval_*.sh` scripts.
5. Run `research/scripts/schematiq/setup_schematiq.sh` before the ScheMatiQ baseline.
   It clones the pinned third-party baseline into a gitignored directory.
6. Open the notebooks after results have been generated.

The expert question files implement the paper's pre-registered-style coverage
protocol: experts independently write atomic, text-answerable questions from a
fixed dialogue, and an LLM judge determines which questions a schema covers.
