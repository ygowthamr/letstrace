#!/usr/bin/env bash
# Force the correct Python version
PYTHON_VERSION=3.12.3

echo "Using Python $PYTHON_VERSION"

# Set up virtual environment using specific Python version
pyenv install -s $PYTHON_VERSION
pyenv global $PYTHON_VERSION

pip install -r requirements.txt