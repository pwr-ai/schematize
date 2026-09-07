#!/usr/bin/env bash
set -uo pipefail

MODELS=(
    claude-sonnet-4.6
    gpt-5.4-nano
    gpt-5.4-mini
    gpt-5.4
    llama-4-scout-17b
    qwen3.6-35b-a3b
    gemma-4-e4b-it
)
CASES=(pl_age pl_personal_rights pl_medical_errors)
VARIANTS=(query_only full_dialogue)

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$(dirname "$(dirname "$(dirname "$SCRIPT_DIR")")")"

MAX_ATTEMPTS=5

run_with_retries() {
    local model="$1" case="$2" dialogue_flag="$3"
    local attempt=1
    while (( attempt <= MAX_ATTEMPTS )); do
        echo "=== Baseline: ScheMatiQ / ${model} / ${case} (attempt ${attempt}/${MAX_ATTEMPTS}) ==="
        uv run python research/scripts/schematiq/run_schematiq_baseline.py --case "${case}" --model "${model}" "${dialogue_flag}" && return 0
        echo "=== Baseline: ScheMatiQ / ${model} / ${case} failed (attempt ${attempt}/${MAX_ATTEMPTS}) ==="
        (( attempt++ ))
    done
    return 1
}

exit_code=0

for model in "${MODELS[@]}"; do
    for variant in "${VARIANTS[@]}"; do
        dialogue_flag="--full-dialogue"
        if [[ "${variant}" == "query_only" ]]; then
            dialogue_flag="--no-full-dialogue"
        fi
        pids=()
        for case in "${CASES[@]}"; do
            run_with_retries "${model}" "${case}" "${dialogue_flag}" &
            pids+=("$!")
        done
        for pid in "${pids[@]}"; do
            wait "${pid}" || exit_code=1
        done
    done
done

exit "${exit_code}"
