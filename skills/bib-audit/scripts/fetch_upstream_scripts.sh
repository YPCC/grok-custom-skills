#!/usr/bin/env bash
# Fetch the full Python scripts for bib-audit from the upstream isaaccorley/skills repo.
# Run from skills/bib-audit/ after cloning this repository.
set -euo pipefail
BASE="https://raw.githubusercontent.com/isaaccorley/skills/main/plugins/bib-audit/skills/bib-audit"
mkdir -p scripts references tests
for f in \
  scripts/audit_refs.py \
  scripts/bibmeta.py \
  scripts/bibstyle.py \
  scripts/lookup_id.py \
  scripts/refparse.py \
  scripts/resolve_refs.py \
  scripts/validate_refs.py \
  references/metadata-apis.md \
  tests/test_regressions.py
do
  echo "Fetching $f ..."
  curl -fsSL "$BASE/$f" -o "$f"
done
echo "Done. scripts/triage.py is already complete in this repo."
python3 -m unittest discover -s tests -v 2>&1 | tail -5 || true
