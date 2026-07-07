#!/usr/bin/env bash
set -uo pipefail

MODELS=(
    # claude-sonnet-4.6
    # gpt-5.4-nano
    # gpt-5.4-mini
    # gpt-5.4
    # llama-4-scout-17b
    # qwen3.6-35b-a3b
    google/gemma-4-e4b-it
    )
CASES=( pl_personal_rights) # pl_age pl_medical_errors
FULL_DIALOGUE_FLAG="--full-dialogue" # "--no-full-dialogue" # 

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$(dirname "$SCRIPT_DIR")"

MAX_ATTEMPTS=5

run_with_retries() {
    local model="$1" case="$2"
    local attempt=1
    while (( attempt <= MAX_ATTEMPTS )); do
        echo "=== Baseline: ScheMatiQ / ${model} / ${case} (attempt ${attempt}/${MAX_ATTEMPTS}) ==="
        uv run python baselines/run_schematiq_baseline.py --case "${case}" --model "${model}" ${FULL_DIALOGUE_FLAG} && return 0
        echo "=== Baseline: ScheMatiQ / ${model} / ${case} failed (attempt ${attempt}/${MAX_ATTEMPTS}) ==="
        (( attempt++ ))
    done
    return 1
}

exit_code=0

for model in "${MODELS[@]}"; do
    pids=()
    for case in "${CASES[@]}"; do
        run_with_retries "${model}" "${case}" &
        pids+=("$!")
    done
    for pid in "${pids[@]}"; do
        wait "${pid}" || exit_code=1
    done
done

exit "${exit_code}"
