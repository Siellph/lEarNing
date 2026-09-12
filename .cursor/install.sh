#!/usr/bin/env bash
# Idempotent bootstrap for the Cloud Agent development environment.
# Installs uv (Python package/venv manager) and prepares a project
# environment, adapting to whichever Python dependency files exist.
set -euo pipefail

export PATH="$HOME/.local/bin:$PATH"

if ! command -v uv >/dev/null 2>&1; then
  echo "Installing uv..."
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.local/bin:$PATH"
fi

echo "Using uv $(uv --version)"

cd "$(dirname "$0")/.."

if [ -f pyproject.toml ] || [ -f uv.lock ]; then
  echo "Found pyproject.toml/uv.lock -> syncing project dependencies."
  uv sync
elif [ -f requirements.txt ]; then
  echo "Found requirements.txt -> installing into .venv."
  uv venv .venv
  uv pip install --python .venv -r requirements.txt
else
  echo "No dependency files found -> ensuring an empty .venv is ready."
  if [ ! -x .venv/bin/python ]; then
    uv venv .venv
  fi
fi

echo "Environment ready. Python: $(.venv/bin/python --version 2>/dev/null || python3 --version)"
