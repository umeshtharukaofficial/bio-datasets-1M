#!/bin/bash

REPO_DIR="/home/Asus/bio-datasets-1M"
cd "$REPO_DIR" || exit 1

echo "Checking git status..."
# Check if there are uncommitted changes (excluding deleted files)
if [ -z "$(git status --porcelain | grep -v '^[ D]D' | grep -v '^ D')" ]; then
    echo "✅ All changes are pushed! Cleaning local storage except the latest commit..."
    ./.venv/bin/python scripts/clean_storage.py
else
    echo "⚠️ Warning: You have uncommitted or unpushed changes. Push them first before cleaning storage!"
fi
