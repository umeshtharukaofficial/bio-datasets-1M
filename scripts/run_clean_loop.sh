#!/bin/bash

REPO_DIR="/home/Asus/bio-datasets-1M"
cd "$REPO_DIR" || exit 1

echo "Starting clean storage loop daemon (runs every 30 minutes)..."

while true; do
    echo "======================================"
    echo "Running cleanup at $(date)"
    ./scripts/clean_storage.sh
    echo "Sleeping for 30 minutes..."
    sleep 1800
done
