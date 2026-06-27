#!/usr/bin/env bash
set -euo pipefail

MODEL=${1:-gpt-5.4-mini}
GENERATION_MODEL=${2:-gpt-5.4-nano}
CASE=${3:-pl_age}

echo "Evaluating history for ${MODEL} / ${CASE}"
uv run python scripts/evaluate_schema.py \
    "case_name=${CASE}" \
    "model_name=${MODEL}" \
    "generation_model_name=${GENERATION_MODEL}" \
    "final_only=false"
