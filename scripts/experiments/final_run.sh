#!/usr/bin/env bash
set -euo pipefail

CASES=(pl_age pl_personal_rights pl_medical_errors)
MODELS=(
    gpt-5.4-nano
    # gpt-5.4-mini
    # gpt-5.2
    # meta-llama/Llama-4-Scout-17B-16E-Instruct
    # Qwen/Qwen3.6-35B-A3B
    # google/gemma-4-26B-A4B-it
    # claude-sonnet-4-6
    # claude-opus-4-7
)

for model in "${MODELS[@]}"; do
    for case in "${CASES[@]}"; do
        echo "Running ${model} for ${case}"
        uv run python scripts/schema_generator_mocked.py \
            "case=${case}" \
            "model_name=${model}"
    done
done
