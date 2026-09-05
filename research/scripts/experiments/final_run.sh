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
NO_REASONING_EFFORT_MODELS=(
    qwen3.6-35b-a3b
)

for model in "${MODELS[@]}"; do
    extra_args=()
    for no_re_model in "${NO_REASONING_EFFORT_MODELS[@]}"; do
        if [[ "${model}" == "${no_re_model}" ]]; then
            extra_args+=("++llm.reasoning_effort=null")
            break
        fi
    done

    for case in "${CASES[@]}"; do
        echo "Running ${model} for ${case}"
        uv run python research/scripts/schema_generator_mocked.py \
            "case=${case}" \
            "model_name=${model}" \
            "${extra_args[@]}"
    done
done
