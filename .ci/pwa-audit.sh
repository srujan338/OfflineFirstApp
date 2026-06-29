#!/usr/bin/env bash
# .ci/pwa-audit.sh — PWA validation using Lighthouse CI
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [pwa] Installing dependencies..."
npm ci --prefer-offline

echo "==> [pwa] Starting preview server in background..."
npm run preview &
PREVIEW_PID=$!

# Wait for preview server (max 30s)
npx wait-on http://localhost:4173 --timeout 30000 || {
  echo "ERROR: Preview server did not start"
  kill $PREVIEW_PID 2>/dev/null || true
  exit 1
}

echo "==> [pwa] Running Lighthouse PWA audit..."
npm run pwa:audit

# Cleanup
kill $PREVIEW_PID 2>/dev/null || true

echo "==> [pwa] PWA audit passed ✓"