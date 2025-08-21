#!/usr/bin/env bash
set -euo pipefail

# Required env vars:
# REPO_URL (e.g. https://github.com/YourUser/YourRepo)
# RUNNER_TOKEN (short-lived registration token)
# Optional env vars:
# RUNNER_NAME, RUNNER_LABELS (comma separated)

REPO_URL="${REPO_URL:-}"
TOKEN="${GITHUB_RUNNER_TOKEN:-}"
RUNNER_NAME="${RUNNER_NAME:-$(hostname)}"
LABELS="${RUNNER_LABELS:-self-hosted,linux}"
ACTIONS_DIR="/actions-runner"
RUNNER_WORK="${RUNNER_WORK:-/runner/_work}"

if [[ -z "$REPO_URL" || -z "$TOKEN" ]]; then
  echo "ERROR: REPO_URL and RUNNER_TOKEN are required environment variables."
  exit 1
fi

cd "$ACTIONS_DIR"

_cleanup() {
  echo "Removing runner..."
  # Best-effort unregister; token may be expired but attempt
  ./config.sh remove --unattended --token "$TOKEN" || true
  exit 0
}
trap _cleanup SIGINT SIGTERM

# Configure the runner (unattended)
./config.sh --unattended \
  --url "$REPO_URL" \
  --token "$TOKEN" \
  --name "$RUNNER_NAME" \
  --labels "$LABELS" \
  --work "$RUNNER_WORK"

# Run the runner (blocks)
./run.sh