#!/usr/bin/env bash
# .ci/bundle-analyze.sh — Bundle size check
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [bundle] Installing dependencies..."
npm ci --prefer-offline

echo "==> [bundle] Running production build..."
npm run build

echo "==> [bundle] Running bundle size analysis..."
npm run bundle:analyze

echo "==> [bundle] Bundle size check passed ✓"