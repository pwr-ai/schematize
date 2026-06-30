#!/usr/bin/env bash
set -euo pipefail

EVAL_MODEL=${1:-gpt-5.4-mini}
GENERATION_MODEL=${2:-gpt-5.4-nano}
CASES=(pl_age pl_personal_rights pl_medical_errors)

for case in "${CASES[@]}"; do
    echo "=== Evaluate baseline: ${GENERATION_MODEL} / ${case} ==="
    uv run python scripts/evaluate_schema.py \
        "case_name=${case}" \
        "model_name=${EVAL_MODEL}" \
        "generation_model_name=baseline/${GENERATION_MODEL}" \
        "state_dir=outputs/baseline/${GENERATION_MODEL}/${case}" \
        "final_only=true"
done
