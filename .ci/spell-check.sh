#!/usr/bin/env bash
# .ci/spell-check.sh — Spell check using codespell
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [spell-check] Installing dependencies..."
npm ci --prefer-offline

echo "==> [spell-check] Running spell check..."
npm run spell:check || {
  echo "ERROR: Spell check found issues. Fix them or add to exceptions in .codespellrc."
  exit 1
}

echo "==> [spell-check] Spell check passed ✓"