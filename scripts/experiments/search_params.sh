#!/usr/bin/env bash
set -euo pipefail

CASES=(pl_medical_errors) # (pl_age pl_personal_rights)
MODELS=(gpt-5.4-nano)

for model in "${MODELS[@]}"; do
    for case in "${CASES[@]}"; do
        echo "Running ${model} for ${case}"
        uv run python scripts/schema_generator_mocked.py \
            "case=${case}" \
            "model_name=${model}" \
            "--multirun"
    done
done
