#!/usr/bin/env bash
set -euo pipefail

MODEL=${1:-gpt-5.4-nano}
GENERATION_MODEL=${2:-gpt-5.4-nano}
CASES=(pl_age pl_personal_rights)

for case in "${CASES[@]}"; do
    echo "Evaluating multirun ${MODEL} / ${GENERATION_MODEL} / ${case}"
    uv run python scripts/evaluate_schema.py \
        "case_name=${case}" \
        "model_name=${MODEL}" \
        "generation_model_name=${GENERATION_MODEL}" \
        "final_only=true"
done
