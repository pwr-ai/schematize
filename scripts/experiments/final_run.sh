#!/usr/bin/env bash
set -euo pipefail

CASES=(pl_age pl_personal_rights pl_medical_errors)
MODELS=(
    claude-sonnet-4.6
    gpt-5.4-nano
    gpt-5.4-mini
    gpt-5.4
    llama-4-scout-17b
    qwen3.6-35b-a3b
    gemma-4-e4b-it
)

for model in "${MODELS[@]}"; do
    for case in "${CASES[@]}"; do
        echo "Running ${model} for ${case}"
        uv run python scripts/schema_generator_mocked.py \
            "case=${case}" \
            "model_name=${model}"\
            "++llm.reasoning_effort=null"
    done
done
