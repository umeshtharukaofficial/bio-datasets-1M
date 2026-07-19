#!/usr/bin/env python3
import os
import sys

# Ensure scripts directory is in path for imports
scripts_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(scripts_dir)

from generate_dataset import main as run_generator, get_next_id_and_total

def main():
    batch_size = int(os.getenv("BATCH_SIZE", "200"))
    manifest_path = "manifest/index.csv"
    
    _, current_total = get_next_id_and_total(manifest_path)
    
    if current_total >= 1_000_000:
        print("Target of 1,000,000 datasets reached. Stopping.")
        sys.exit(0)
        
    print(f"Starting batch runner. Current total: {current_total}. Target batch size: {batch_size}")
    
    generated = 0
    for i in range(batch_size):
        _, current_total = get_next_id_and_total(manifest_path)
        if current_total >= 1_000_000:
            print("Target of 1,000,000 datasets reached during batch. Stopping.")
            break
        run_generator()
        generated += 1
        
    print(f"Batch runner completed. Generated {generated} new datasets in this batch.")

if __name__ == "__main__":
    main()
