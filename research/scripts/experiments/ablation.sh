#!/usr/bin/env bash
set -euo pipefail

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
CASES=(pl_age pl_personal_rights pl_medical_errors)

run_ablation() {
    local model=$1 case=$2 skip_pd=$3 skip_sr=$4 skip_dg=$5
    shift 5
    local extra_args=("$@")
    local combo="pd${skip_pd^}_sr${skip_sr^}_dg${skip_dg^}"
    local state_file="outputs/ablation/generated_schemas/${model}/${case}/${combo}/state.json"

    if [[ -f "${state_file}" ]]; then
        echo "--- Skipping ${model} / ${case} / ${combo} (state.json exists) ---"
        return
    fi

    echo "--- Running ${model} / ${case} / ${combo} ---"
    uv run python research/scripts/schema_generator_ablation.py case="${case}" model_name="${model}" "${extra_args[@]}" \
        schema_generator.skip_problem_definition="${skip_pd}" \
        schema_generator.skip_refinement="${skip_sr}" \
        schema_generator.skip_data_grounded="${skip_dg}"
}

pids=()

for model in "${MODELS[@]}"; do
    extra_args=()
    for no_re_model in "${NO_REASONING_EFFORT_MODELS[@]}"; do
        if [[ "${model}" == "${no_re_model}" ]]; then
            extra_args+=("++llm.model_kwargs.reasoning_effort=null")
            break
        fi
    done

    for case in "${CASES[@]}"; do
        echo "=== Ablation: ${model} / ${case} ==="

        run_ablation "${model}" "${case}" true false false "${extra_args[@]}" &   # No problem definition
        pids+=("$!")
        run_ablation "${model}" "${case}" false true false "${extra_args[@]}" &   # No schema refinement
        pids+=("$!")
        run_ablation "${model}" "${case}" false false true "${extra_args[@]}" &   # No data-grounded refinement
        pids+=("$!")
        run_ablation "${model}" "${case}" true true false "${extra_args[@]}" &    # No problem definition + no schema refinement
        pids+=("$!")
        run_ablation "${model}" "${case}" true false true "${extra_args[@]}" &    # No problem definition + no data-grounded refinement
        pids+=("$!")
        run_ablation "${model}" "${case}" false true true "${extra_args[@]}" &    # No schema refinement + no data-grounded refinement
        pids+=("$!")
        run_ablation "${model}" "${case}" true true true "${extra_args[@]}" &     # No problem definition + no schema refinement + no data-grounded refinement
        pids+=("$!")
    done
done

exit_code=0
for pid in "${pids[@]}"; do
    wait "${pid}" || exit_code=1
done

exit "${exit_code}"
