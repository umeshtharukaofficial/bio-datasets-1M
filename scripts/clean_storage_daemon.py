#!/usr/bin/env python3
import os
import subprocess
import time
import sys

# Get base directory of the repository
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(base_dir)

print(f"[{time.ctime()}] Starting clean storage daemon (runs every 30 minutes)...")

while True:
    try:
        # Check git status first
        status_proc = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Check if there are uncommitted changes, ignoring deleted files
        uncommitted = False
        for line in status_proc.stdout.splitlines():
            # If the change is not a deleted file, it is considered uncommitted
            if line and not (line.startswith(" D") or line.startswith("D ")):
                uncommitted = True
                break
                
        if not uncommitted:
            # Get latest commit files
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
                    
            if latest_files:
                deleted_count = 0
                kept_count = 0
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
                print(f"[{time.ctime()}] Cleanup finished. Deleted {deleted_count} files, kept {kept_count} files.")
            else:
                print(f"[{time.ctime()}] Warning: No CSV files in latest commit. Skipping deletion.")
        else:
            print(f"[{time.ctime()}] Skipping cleanup: there are uncommitted changes.")
    except Exception as e:
        print(f"[{time.ctime()}] Error during cleanup: {e}")
        
    sys.stdout.flush()
    time.sleep(1800)
