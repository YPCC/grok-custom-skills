#!/usr/bin/env bash
# Re-install skills from https://github.com/addyosmani/agent-skills
set -euo pipefail
DEST="$(cd "$(dirname "$0")" && pwd)"
TMP="${TMPDIR:-/tmp}/addyosmani-agent-skills"
git clone --depth 1 https://github.com/addyosmani/agent-skills.git "$TMP"
COMMIT=$(git -C "$TMP" rev-parse HEAD)
COMMIT_DATE=$(git -C "$TMP" log -1 --format='%ci')
for skill_dir in "$TMP"/skills/*/; do
  skill_name=$(basename "$skill_dir")
  target="$DEST/$skill_name"
  rm -rf "$target"
  cp -R "$skill_dir" "$target"
  cat > "$target/SOURCE.md" <<EOF
# Skill source

| Field | Value |
|-------|-------|
| Repository | https://github.com/addyosmani/agent-skills |
| Skill path | skills/$skill_name |
| Installed commit | \`$COMMIT\` |
| Commit date | $COMMIT_DATE |
| License | See repository LICENSE |

Do not edit files here for local customizations — re-install from upstream or fork the repo.
EOF
done
echo "Installed $(find "$DEST" -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ') skills from $COMMIT"
