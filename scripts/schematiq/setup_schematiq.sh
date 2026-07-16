#!/usr/bin/env bash
# Clone ScheMatiQ (pinned) and install schematiq-lib into the uv environment.
# Usage: bash scripts/schematiq/setup_schematiq.sh [ref]
set -euo pipefail

REPO_URL="https://github.com/shaharl6000/ScheMatiQ"
# Commit used for the baseline results (2026-07-06); pass a ref to override.
REF="${1:-dc8f93d941840ae4e15f1ed3cc53b52312049229}"

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"
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
  API_KEY=<litellm-key> API_URL=http://localhost:4000 bash scripts/schematiq/baseline_schematiq.sh
  API_KEY=<litellm-key> API_URL=http://localhost:4000 bash scripts/schematiq/eval_schematiq.sh
EOF
