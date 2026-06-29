#!/usr/bin/env bash
# .ci/test.sh — Vitest unit tests with coverage
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [test] Installing dependencies..."
npm ci --prefer-offline

echo "==> [test] Running Vitest unit tests with coverage..."
npm run test -- --coverage --reporter=verbose

echo "==> [test] Unit tests passed ✓"