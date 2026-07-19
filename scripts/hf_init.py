import os
from huggingface_hub import HfApi, create_repo
HF_TOKEN = os.environ["HF_TOKEN"]
HF_USERNAME = os.environ.get("HF_USERNAME") or HfApi(token=HF_TOKEN).whoami()["name"]
REPO_ID = f"{HF_USERNAME}/bio-datasets-1M"
create_repo(
    repo_id=REPO_ID,
    repo_type="dataset",
    private=False,
    exist_ok=True,
    token=HF_TOKEN,
)
print(f" HuggingFace dataset ready: https://huggingface.co/datasets/{REPO_ID}")
