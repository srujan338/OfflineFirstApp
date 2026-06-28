#!/usr/bin/env bash
# .ci/deploy.sh -- Deployment script for ReceiptAI
# Handles both preview (MR/PR) and production deployments.
#
# Usage:
#   .ci/deploy.sh preview    -- Deploy preview for merge request
#   .ci/deploy.sh production -- Deploy to production (manual gate)
#
# Modify this script to target your actual hosting platform (Vercel, Netlify,
# GitHub Pages, GitLab Pages, S3, etc.).

set -euo pipefail

DEPLOY_ENV=${1:-preview}

echo "==> [deploy] Starting deployment: ${DEPLOY_ENV}"

case "${DEPLOY_ENV}" in
  preview)
    echo "==> [deploy] Deploying preview for merge request..."
    # Example: Deploy to GitLab Pages review site or Vercel preview
    # vercel deploy --target preview --yes
    ;;
  production)
    echo "==> [deploy] Deploying to production..."
    # Example: Deploy to GitHub Pages, Netlify, or Vercel
    # vercel deploy --target production --yes --prod
    ;;
  *)
    echo "==> [deploy] ERROR: Unknown deploy environment '${DEPLOY_ENV}'. Valid options: preview, production"
    exit 1
    ;;
esac

echo "==> [deploy] Deployment to ${DEPLOY_ENV} complete."
