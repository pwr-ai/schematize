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

for generation_model in "${GENERATION_MODELS[@]}"; do
    for case in "${CASES[@]}"; do
        echo "=== Evaluate baseline: ${generation_model} / ${case} ==="
        uv run python scripts/evaluate_schema.py \
            "case_name=${case}" \
            "model_name=${EVAL_MODEL}" \
            "generation_model_name=baseline/${generation_model}" \
            "state_dir=outputs/baseline/${generation_model}/${case}" \
            "output_subdir=baseline_evaluation/${EVAL_MODEL}/${generation_model}/${case}" \
            "final_only=true"
    done
done
