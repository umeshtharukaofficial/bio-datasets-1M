---
license: cc0-1.0
task_categories:
- tabular-classification
- tabular-regression
language:
- en
tags:
- biology
- genomics
- proteomics
- ecology
- education
- synthetic
pretty_name: Bio Datasets 1M
size_categories:
- 100K<n<1M
---

# 🧬 Bio Datasets 1M

Open collection of up to 1,000,000 synthetic biology datasets for students worldwide.

Auto-updated every 5 minutes from GitHub: https://github.com/umeshtharukaofficial/bio-datasets-1M

## Categories

Genomics · Proteomics · Ecology · Microbiology · Botany · Zoology · Cell Biology · Neuroscience · Biochemistry · Bioinformatics

## Load in Python

```python
from huggingface_hub import hf_hub_download
import pandas as pd

path = hf_hub_download(
    repo_id="umeshtharukaofficial/bio-datasets-1M",
    filename="datasets/genomics/genomics_000123_variant.csv",
    repo_type="dataset",
)
df = pd.read_csv(path)
```

## License

CC0-1.0 — public domain. Free to use, remix, and publish.
Data is synthetic and for learning only — not for clinical use.
