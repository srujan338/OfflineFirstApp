#!/usr/bin/env bash
# .ci/type-check.sh — TypeScript strict mode check
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [type-check] Installing dependencies..."
npm ci --prefer-offline

echo "==> [type-check] Running TypeScript strict mode..."
npm run type-check

echo "==> [type-check] TypeScript check passed ✓"