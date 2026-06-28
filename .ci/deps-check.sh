#!/usr/bin/env bash
# .ci/deps-check.sh — Check for outdated dependencies
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [deps-check] Installing dependencies..."
npm ci --prefer-offline

echo "==> [deps-check] Checking for outdated dependencies..."
npm run deps:check || {
  echo "WARNING: New versions of dependencies are available."
  echo "Update with: npm update"
  # Allow failure for this check (warn-only)
}

echo "==> [deps-check] Dependency freshness check complete ✓"