#!/usr/bin/env bash
set -euo pipefail

CASES=(pl_age pl_personal_rights pl_medical_errors)
# The paper's hyperparameter search uses gpt-5.4-nano only.
MODELS=(gpt-5.4-nano)

for model in "${MODELS[@]}"; do
    for case in "${CASES[@]}"; do
        echo "Running ${model} for ${case}"
        uv run python research/scripts/schema_generator_mocked.py \
            "case=${case}" \
            "model_name=${model}" \
            "--multirun"
    done
done
