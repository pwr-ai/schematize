#!/usr/bin/env bash
set -euo pipefail

MODEL=${1:-gpt-5.4-mini}
CASES=(pl_age pl_personal_rights pl_medical_errors)

for case in "${CASES[@]}"; do
    echo "=== Baseline: ${MODEL} / ${case} ==="
    uv run python scripts/baseline.py --case "${case}" --model "${MODEL}"
done
