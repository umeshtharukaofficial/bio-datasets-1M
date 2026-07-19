import os
import shutil
import pathlib
from huggingface_hub import HfApi, upload_folder, create_repo

HF_TOKEN = os.environ["HF_TOKEN"]
api = HfApi(token=HF_TOKEN)
HF_USERNAME = os.environ.get("HF_USERNAME") or api.whoami()["name"]
REPO_ID = f"{HF_USERNAME}/bio-datasets-1M"

# Ensure repo exists
create_repo(repo_id=REPO_ID, repo_type="dataset", private=False, exist_ok=True, token=HF_TOKEN)

# Copy the HF dataset card into the root before upload
shutil.copy("hf/README.md", "README_HF_TMP.md")

# Determine patterns to allow
is_full_sync = os.environ.get("HF_FULL_SYNC", "").lower() in ("true", "1", "yes")

if is_full_sync:
    print("Running FULL consistency sync...")
    allow_patterns = [
        "datasets/**",
        "manifest/index.csv",
        "README_HF_TMP.md",
    ]
else:
    print("Running INCREMENTAL sync...")
    batch_size = int(os.environ.get("BATCH_SIZE", "200"))
    
    # Read the last N rows of manifest/index.csv to get the files of the last batch
    last_files = []
    manifest_path = pathlib.Path("manifest/index.csv")
    if manifest_path.exists():
        with open(manifest_path, "r", encoding="utf-8") as f:
            lines = f.readlines()
            # The header is the first line
            data_lines = lines[1:]
            # Get the last batch_size lines
            last_lines = data_lines[-batch_size:]
            for line in last_lines:
                parts = line.strip().split(",")
                if len(parts) >= 3:
                    # id,category,filename,rows,created_at
                    category = parts[1]
                    filename = parts[2]
                    last_files.append(f"datasets/{category}/{filename}")
                    
    print(f"Found {len(last_files)} files from the last batch to upload.")
    allow_patterns = [
        "manifest/index.csv",
        "README_HF_TMP.md",
    ] + last_files

try:
    # Upload the datasets/ and manifest/ folders + README
    upload_folder(
        repo_id=REPO_ID,
        repo_type="dataset",
        folder_path=".",
        allow_patterns=allow_patterns,
        path_in_repo=".",
        commit_message="auto-sync from GitHub batch",
        token=HF_TOKEN,
    )

    # Rename the uploaded card on HF so its README shows correctly
    api.upload_file(
        path_or_fileobj="hf/README.md",
        path_in_repo="README.md",
        repo_id=REPO_ID,
        repo_type="dataset",
        commit_message="update dataset card",
        token=HF_TOKEN,
    )
    print(f"Synced to HuggingFace: https://huggingface.co/datasets/{REPO_ID}")
finally:
    # Clean up temporary README copy
    if os.path.exists("README_HF_TMP.md"):
        os.remove("README_HF_TMP.md")
