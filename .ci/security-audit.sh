#!/usr/bin/env bash
# .ci/security-audit.sh — npm audit + Snyk security scan
# Both GitLab CI and GitHub Actions use this script

set -euo pipefail

echo "==> [security] Installing dependencies..."
npm ci --prefer-offline

echo "==> [security] Running npm audit (audit-level=high)..."
npm audit --audit-level=high || {
  echo "ERROR: High severity vulnerabilities found in dependencies."
  exit 1
}

echo "==> [security] npm audit passed ✓"

# Only run Snyk if SNYK_TOKEN is set
if [ -n "${SNYK_TOKEN:-}" ]; then
  echo "==> [security] Running Snyk security scan..."
  npm run security:snyk || {
    echo "WARNING: Snyk scan failed or found vulnerabilities."
    exit 1
  }
  echo "==> [security] Snyk scan passed ✓"
else
  echo "==> [security] SNYK_TOKEN not set, skipping Snyk scan."
fi