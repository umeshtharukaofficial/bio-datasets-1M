#!/usr/bin/env python3
import os
import subprocess
import sys

# Get base directory of the repository
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base_dir)

print("Starting storage cleanup...")

try:
    # Get the list of CSV files in the latest commit
    result = subprocess.run(
        ["git", "show", "--name-only", "--pretty=", "HEAD"],
        capture_output=True,
        text=True,
        check=True
    )
    latest_files = set()
    for line in result.stdout.splitlines():
        line = line.strip()
        if line.endswith(".csv"):
            latest_files.add(line)

    if not latest_files:
        print("No CSV files found in the latest commit. Aborting cleanup to protect data.")
        sys.exit(1)

    print(f"Found {len(latest_files)} CSV files in the latest commit to keep.")

    deleted_count = 0
    kept_count = 0
    
    # Walk through datasets/ and delete any CSV file not in the latest_files set
    for root, dirs, files in os.walk("datasets"):
        for file in files:
            if file.endswith(".csv"):
                full_path = os.path.join(root, file)
                rel_path = os.path.relpath(full_path, base_dir).replace(os.sep, "/")
                if rel_path in latest_files:
                    kept_count += 1
                else:
                    os.remove(full_path)
                    deleted_count += 1

    print(f"Cleanup finished. Deleted {deleted_count} files, kept {kept_count} files.")
except Exception as e:
    print(f"Error during cleanup: {e}")
    sys.exit(1)
