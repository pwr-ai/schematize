#!/usr/bin/env bash
set -euo pipefail

MODEL=${1:-gpt-5.4-nano}
CASES=(pl_age pl_personal_rights pl_medical_errors)

for case in "${CASES[@]}"; do
    echo "=== Ablation: ${MODEL} / ${case} ==="

    echo "--- Baseline (all components enabled) ---"
    uv run python scripts/schema_generator_ablation.py +case="${case}" model_name="${MODEL}"

    echo "--- No problem definition ---"
    uv run python scripts/schema_generator_ablation.py +case="${case}" model_name="${MODEL}" \
        schema_generator.skip_problem_definition=true

    echo "--- No schema refinement ---"
    uv run python scripts/schema_generator_ablation.py +case="${case}" model_name="${MODEL}" \
        schema_generator.skip_refinement=true

    echo "--- No data-grounded refinement ---"
    uv run python scripts/schema_generator_ablation.py +case="${case}" model_name="${MODEL}" \
        schema_generator.skip_data_grounded=true
done
