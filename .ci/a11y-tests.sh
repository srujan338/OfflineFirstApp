#!/usr/bin/env bash
# .ci/a11y-tests.sh — Accessibility tests using axe-core + Playwright
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [a11y] Installing dependencies..."
npm ci --prefer-offline

echo "==> [a11y] Installing Playwright browsers..."
npx playwright install --with-deps chromium

echo "==> [a11y] Starting preview server in background..."
npm run preview &
PREVIEW_PID=$!

# Wait for preview server to be ready (max 30s)
echo "==> [a11y] Waiting for preview server..."
npx wait-on http://localhost:4173 --timeout 30000 || {
  echo "ERROR: Preview server did not start"
  kill $PREVIEW_PID 2>/dev/null || true
  exit 1
}

echo "==> [a11y] Running accessibility tests..."
npm run test:a11y

# Cleanup
kill $PREVIEW_PID 2>/dev/null || true

echo "==> [a11y] Accessibility tests passed ✓"