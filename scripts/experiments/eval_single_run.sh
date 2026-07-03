#!/usr/bin/env bash
set -euo pipefail

MODEL=${1:-gpt-5.4-mini}
GENERATION_MODELS=(
    # gpt-5.4-nano
    # gpt-5.4-mini
    # gpt-5.4
    llama-4-scout-17b
    qwen3.6-35b-a3b
    # # google/gemma-4-26B-A4B-it
    # claude-sonnet-4.6
    # claude-opus-4-7
)
CASES=(pl_age pl_personal_rights pl_medical_errors)

for gen_model in "${GENERATION_MODELS[@]}"; do
    for case in "${CASES[@]}"; do
        echo "Evaluating history for ${MODEL} / ${gen_model} / ${case}"
        uv run python scripts/evaluate_schema.py \
            "case_name=${case}" \
            "model_name=${MODEL}" \
            "generation_model_name=${gen_model}" \
            "state_dir=outputs/generated_schemas/${gen_model}/${case}" \
            "final_only=false" \
            "hydra.run.dir=outputs/evaluation/single_run/${MODEL}/${gen_model}/${case}"
    done
done
