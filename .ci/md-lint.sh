#!/usr/bin/env bash
# .ci/md-lint.sh — Markdown lint check
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [md-lint] Running markdown lint..."
npm run md:lint || {
  echo "ERROR: Markdown lint failed. Fix the issues above."
  exit 1
}

echo "==> [md-lint] Markdown lint passed ✓"