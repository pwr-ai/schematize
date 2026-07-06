#!/usr/bin/env bash
# Clone ScheMatiQ (pinned) and install schematiq-lib into the uv environment.
# Usage: bash baselines/setup_schematiq.sh [ref]
set -euo pipefail

REPO_URL="https://github.com/shaharl6000/ScheMatiQ"
# Commit used for the baseline results (2026-07-06); pass a ref to override.
REF="${1:-dc8f93d941840ae4e15f1ed3cc53b52312049229}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$SCRIPT_DIR")"
TARGET="$SCRIPT_DIR/ScheMatiQ"

if [[ ! -d "$TARGET/.git" ]]; then
    git clone "$REPO_URL" "$TARGET"
fi
git -C "$TARGET" fetch --all --quiet
git -C "$TARGET" checkout --quiet "$REF"
echo "ScheMatiQ at $(git -C "$TARGET" rev-parse HEAD)"

cd "$REPO_ROOT"
uv sync --extra huggingface --extra scripts
uv pip install -e "$TARGET/schematiq-lib"

uv run python -c "import schematiq; print('schematiq', schematiq.__version__, 'OK')"

cat <<'EOF'

Next steps:
  OMP_NUM_THREADS=1 OPENAI_API_KEY=<litellm-key> OPENAI_BASE_URL=http://localhost:4000 \
    uv run python baselines/run_schematiq_baseline.py --model gpt-5.4-mini
  # then evaluate with scripts/evaluate_schema.py and upload with
  # baselines/upload_baseline_results.py (needs HF_TOKEN).
EOF
