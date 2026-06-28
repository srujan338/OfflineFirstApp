#!/usr/bin/env bash
# .ci/e2e-tests.sh — Playwright E2E tests
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [e2e] Installing dependencies..."
npm ci --prefer-offline

echo "==> [e2e] Installing Playwright browsers..."
npx playwright install --with-deps chromium

echo "==> [e2e] Starting dev server in background..."
npm run dev &
DEV_PID=$!

# Wait for server to be ready (max 60s)
echo "==> [e2e] Waiting for dev server to be ready..."
npx wait-on http://localhost:5173 --timeout 60000 || {
  echo "ERROR: Dev server did not start within 60 seconds"
  kill $DEV_PID 2>/dev/null || true
  exit 1
}

echo "==> [e2e] Dev server is up. Running E2E tests..."
npm run test:e2e

# Cleanup
kill $DEV_PID 2>/dev/null || true

echo "==> [e2e] E2E tests passed ✓"