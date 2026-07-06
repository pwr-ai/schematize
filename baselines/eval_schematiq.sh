#!/usr/bin/env bash
set -euo pipefail

EVAL_MODEL=${1:-gpt-5.4-mini}
GENERATION_MODELS=(
    claude-sonnet-4.6
    # gpt-5.4-nano
    # gpt-5.4-mini
    # gpt-5.4
    # llama-4-scout-17b
    # qwen3.6-35b-a3b
    # google/gemma-4-e4b-it
    )
CASES=(pl_age pl_personal_rights pl_medical_errors)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$(dirname "$SCRIPT_DIR")"

for generation_model in "${GENERATION_MODELS[@]}"; do
    GENERATION_NAME="schematiq_${generation_model}_full_dialogue"
    for case in "${CASES[@]}"; do
        echo "=== Evaluate ${GENERATION_NAME} / ${case} ==="
        uv run python scripts/evaluate_schema.py \
            "case_name=${case}" \
            "model_name=${EVAL_MODEL}" \
            "generation_model_name=${GENERATION_NAME}" \
            "state_dir=outputs/schematiq/${GENERATION_NAME}/${case}" \
            "final_only=true"
    done
done
