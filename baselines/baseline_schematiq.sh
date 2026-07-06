#!/usr/bin/env bash
set -euo pipefail

MODELS=(
    claude-sonnet-4.6
    gpt-5.4-nano
    # gpt-5.4-mini
    # gpt-5.4
    # llama-4-scout-17b
    # qwen3.6-35b-a3b
    # google/gemma-4-e4b-it
    )
CASES=(pl_age pl_personal_rights pl_medical_errors)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$(dirname "$SCRIPT_DIR")"

for model in "${MODELS[@]}"; do
for case in "${CASES[@]}"; do
        echo "=== Baseline: ScheMatiQ / ${model} / ${case} ==="
        uv run python baselines/run_schematiq_baseline.py --case "${case}" --model "${model}"
    done
done
