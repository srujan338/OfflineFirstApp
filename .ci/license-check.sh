#!/usr/bin/env bash
# .ci/license-check.sh — Check for prohibited licenses in dependencies
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [license-check] Installing dependencies..."
npm ci --prefer-offline

echo "==> [license-check] Checking dependency licenses..."
npm run license:check || {
  echo "ERROR: Prohibited licenses found in dependencies."
  exit 1
}

echo "==> [license-check] License check passed ✓"