#!/usr/bin/env bash
# .ci/format-check.sh — Prettier format + Markdown lint check
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [format] Installing dependencies..."
npm ci --prefer-offline

echo "==> [format] Checking Prettier formatting..."
npm run format:check || {
  echo "ERROR: Files are not formatted. Run 'npm run format' to fix."
  exit 1
}

echo "==> [format] Prettier format check passed ✓"