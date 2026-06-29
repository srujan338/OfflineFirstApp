#!/usr/bin/env bash
# .ci/build.sh — Production build
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [build] Installing dependencies..."
npm ci --prefer-offline

echo "==> [build] Running production build..."
npm run build

echo "==> [build] Verifying dist output..."
# Ensure critical files exist
test -s dist/index.html || { echo "ERROR: dist/index.html not found"; exit 1; }
test -d dist/assets || { echo "ERROR: dist/assets not found"; exit 1; }

echo "==> [build] Production build succeeded ✓"