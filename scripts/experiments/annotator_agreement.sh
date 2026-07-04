#!/usr/bin/env bash
set -euo pipefail

EVAL_MODEL=${1:-gpt-5.4-mini}
CASES=(pl_age pl_personal_rights pl_medical_errors)

for case in "${CASES[@]}"; do
    echo "=== Annotator agreement: ${case} ==="
    uv run python scripts/evaluate_annotator_agreement.py \
        "case_name=${case}" \
        "model_name=${EVAL_MODEL}"
done
