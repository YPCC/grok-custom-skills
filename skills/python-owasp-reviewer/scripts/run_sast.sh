#!/usr/bin/env bash
# Optional SAST helper for python-owasp-reviewer skill.
# Usage: ./scripts/run_sast.sh [target_directory]
set -euo pipefail

TARGET="${1:-.}"
echo "=== Python OWASP SAST — target: $TARGET ==="

if command -v bandit >/dev/null 2>&1; then
  echo ""
  echo "--- Bandit (high/medium) ---"
  bandit -r "$TARGET" -ll -q 2>/dev/null || bandit -r "$TARGET" -ll
else
  echo "Bandit not installed. Install: pip install bandit"
fi

if command -v pip-audit >/dev/null 2>&1; then
  echo ""
  echo "--- pip-audit ---"
  if [[ -f requirements.txt ]]; then
    pip-audit -r requirements.txt || true
  elif [[ -f pyproject.toml ]]; then
    pip-audit || true
  else
    echo "No requirements.txt or pyproject.toml found for pip-audit."
  fi
else
  echo "pip-audit not installed. Install: pip install pip-audit"
fi

echo ""
echo "--- Dangerous pattern grep (sample) ---"
PATTERNS=(
  'os\.system\('
  'shell=True'
  'eval\('
  'pickle\.loads'
  'yaml\.load\('
  'verify=False'
  'allow_origins.*\*'
)

for pat in "${PATTERNS[@]}"; do
  count=$(rg -c "$pat" "$TARGET" --glob '*.py' 2>/dev/null | awk -F: '{s+=$2} END {print s+0}')
  if [[ "${count:-0}" -gt 0 ]]; then
    echo "  [$pat] $count match(es)"
    rg -n "$pat" "$TARGET" --glob '*.py' 2>/dev/null | head -5
  fi
done

echo ""
echo "=== SAST scan complete — manual taint review still required ==="