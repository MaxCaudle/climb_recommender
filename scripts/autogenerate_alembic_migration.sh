#!/usr/bin/env bash
set -euo pipefail

# Autogenerate an Alembic migration using the current git branch name as message
# Usage: scripts/autogenerate_alembic_migration.sh

branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null || true)
if [[ -z "$branch" || "$branch" == "HEAD" ]]; then
  branch=$(git rev-parse --short HEAD 2>/dev/null || true)
fi

# Sanitize branch name for use as a migration message / filename
msg=$(printf "%s" "$branch" | sed -E 's#[/ ]#_#g' | sed -E 's/[^A-Za-z0-9_.\-]/_/g')
if [[ -z "$msg" ]]; then
  msg="autogeneration"
fi

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
repo_root=$(cd "$script_dir/.." && pwd)

ALEMBIC_INI="$repo_root/backend/alembic.ini"
if [[ ! -f "$ALEMBIC_INI" ]]; then
  echo "Error: $ALEMBIC_INI not found" >&2
  exit 1
fi

echo "Generating alembic revision with message: $msg"

# Ensure the repository root is on PYTHONPATH so `import backend` works
if command -v alembic >/dev/null 2>&1; then
  PYTHONPATH="$repo_root" alembic -c "$ALEMBIC_INI" revision --autogenerate -m "$msg"
else
  PYTHONPATH="$repo_root" python -m alembic -c "$ALEMBIC_INI" revision --autogenerate -m "$msg"
fi

echo "Done."
