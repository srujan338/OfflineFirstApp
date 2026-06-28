#!/usr/bin/env bash
# .ci/lint.sh — ESLint + Prettier check
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [lint] Installing dependencies..."
npm ci --prefer-offline

echo "==> [lint] Running ESLint..."
npm run lint

echo "==> [lint] ESLint + Prettier checks passed ✓"