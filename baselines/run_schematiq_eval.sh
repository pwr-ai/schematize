#!/usr/bin/env bash
# End-to-end ScheMatiQ baseline: inference on data/cases → evaluation → HF upload.
#
# Usage:
#   API_KEY=<litellm-key> [API_URL=http://localhost:4000] [HF_TOKEN=hf_...] \
#     bash baselines/run_schematiq_eval.sh [gen_model] [eval_model]
#
# Arguments (positional, following scripts/experiments/ conventions):
#   gen_model   model used by ScheMatiQ for schema discovery (default: gpt-5.4-mini)
#   eval_model  judge model for evaluate_schema.py            (default: gpt-5.4-mini)
#
# Environment:
#   API_URL     OpenAI-compatible endpoint / LiteLLM proxy (default: http://localhost:4000)
#   API_KEY     key for that endpoint (required)
#   HF_TOKEN    HuggingFace token; if unset the upload step is skipped
#   HF_REPO_ID  target dataset repo (default: ktagowski/schematize-schematiq-baseline)
#   SKIP_UPLOAD set to 1 to skip the HF upload
set -euo pipefail

GEN_MODEL="${1:-gpt-5.4-mini}"
EVAL_MODEL="${2:-gpt-5.4-mini}"
API_URL="${API_URL:-http://localhost:4000}"
API_KEY="${API_KEY:?API_KEY is required (LiteLLM proxy / OpenAI key)}"
HF_REPO_ID="${HF_REPO_ID:-ktagowski/schematize-schematiq-baseline}"

CASES=(pl_age pl_medical_errors pl_personal_rights)
GENERATION_NAME="schematiq_${GEN_MODEL}_full_dialogue"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$(dirname "$SCRIPT_DIR")"

echo "=== 1/3 ScheMatiQ inference (${GEN_MODEL} via ${API_URL}) ==="
# OMP_NUM_THREADS=1: faiss-cpu segfaults on macOS arm64 with torch's OpenMP otherwise.
OMP_NUM_THREADS=1 TOKENIZERS_PARALLELISM=false \
OPENAI_API_KEY="$API_KEY" OPENAI_BASE_URL="$API_URL" \
    uv run python baselines/run_schematiq_baseline.py --model "$GEN_MODEL"

echo "=== 2/3 Schema evaluation (judge: ${EVAL_MODEL}) ==="
for case in "${CASES[@]}"; do
    echo "Evaluating ${GENERATION_NAME} / ${case}"
    API_URL="$API_URL" API_KEY="$API_KEY" uv run python scripts/evaluate_schema.py \
        "case_name=${case}" \
        "model_name=${EVAL_MODEL}" \
        "generation_model_name=${GENERATION_NAME}" \
        "final_only=true"
done

if [[ "${SKIP_UPLOAD:-0}" == "1" ]]; then
    echo "=== 3/3 Upload skipped (SKIP_UPLOAD=1) ==="
elif [[ -z "${HF_TOKEN:-}" ]]; then
    echo "=== 3/3 Upload skipped (HF_TOKEN not set) ==="
else
    echo "=== 3/3 Uploading to ${HF_REPO_ID} (private) ==="
    HF_TOKEN="$HF_TOKEN" uv run python baselines/upload_baseline_results.py \
        --generation-name "$GENERATION_NAME" \
        --eval-model "$EVAL_MODEL" \
        --repo-id "$HF_REPO_ID"
fi

echo "Done."
