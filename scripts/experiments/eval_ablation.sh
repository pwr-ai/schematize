#!/usr/bin/env bash
set -euo pipefail

EVAL_MODEL=${1:-gpt-5.4-mini}
MODELS=(
    qwen3.6-35b-a3b
)
CASES=(pl_age pl_personal_rights pl_medical_errors)

run_eval() {
    local model=$1 case=$2 skip_pd=$3 skip_sr=$4 skip_dg=$5
    local combo="pd${skip_pd^}_sr${skip_sr^}_dg${skip_dg^}"
    echo "--- Evaluating ${model} / ${case} / ${combo} ---"
    uv run python scripts/evaluate_schema.py \
        "case_name=${case}" \
        "model_name=${EVAL_MODEL}" \
        "generation_model_name=ablation/${model}" \
        "state_dir=outputs/ablation/generated_schemas/${model}/${case}/${combo}" \
        "output_subdir=ablation_evaluation/${EVAL_MODEL}/${model}/${case}/${combo}" \
        "final_only=true"
}

for model in "${MODELS[@]}"; do
    for case in "${CASES[@]}"; do
        echo "=== Evaluate ablation: ${model} / ${case} ==="

        run_eval "${model}" "${case}" true false false    # No problem definition
        run_eval "${model}" "${case}" false true false    # No schema refinement
        run_eval "${model}" "${case}" false false true      # No data-grounded refinement
        run_eval "${model}" "${case}" true true false      # No problem definition + no schema refinement
        run_eval "${model}" "${case}" true false true      # No problem definition + no data-grounded refinement
        run_eval "${model}" "${case}" false true true        # No schema refinement + no data-grounded refinement
        run_eval "${model}" "${case}" true true true         # No problem definition + no schema refinement + no data-grounded refinement
    done
done
