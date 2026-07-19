#!/usr/bin/env python3
import subprocess
import datetime
import os
import sys

# Get base directory of the repository
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base_dir)

# Determine the python executable to use (prefer the virtualenv one if it exists)
venv_python = os.path.join(base_dir, ".venv", "bin", "python")
python_exec = venv_python if os.path.exists(venv_python) else sys.executable

batch_size = os.getenv("BATCH_SIZE", "200")

print(f"[{datetime.datetime.now().isoformat()}] Starting auto commit script...")

# Run the batch runner
try:
    subprocess.run([python_exec, "scripts/batch_runner.py"], check=True)
except subprocess.CalledProcessError as e:
    print(f"Error running batch runner: {e}")
    sys.exit(1)

# Git operations
try:
    subprocess.run(["git", "add", "."], check=True)
    
    # Check if there are any changes staged
    status_proc = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True)
    if not status_proc.stdout.strip():
        print("No changes to commit.")
        sys.exit(0)
        
    # Get current total count from manifest/index.csv
    total_count = 0
    manifest_path = "manifest/index.csv"
    if os.path.exists(manifest_path):
        try:
            with open(manifest_path, 'r') as f:
                total_count = max(0, sum(1 for _ in f) - 1)
        except Exception:
            pass

    msg = f"chore(data): auto-generate {batch_size} synthetic biology datasets (total: {total_count})"
    subprocess.run(["git", "commit", "-m", msg], check=True)
    print("Committed successfully. Attempting to push...")
    
    push_res = subprocess.run(["git", "push"], capture_output=True, text=True)
    if push_res.returncode == 0:
        print("Pushed successfully.")
    else:
        print(f"Push failed or skipped. Git output:\n{push_res.stderr}\n{push_res.stdout}")
except Exception as e:
    print(f"Git operation failed: {e}")
