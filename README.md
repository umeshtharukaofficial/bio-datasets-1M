# 🧬 Bio-Datasets-1M: 1,000,000 Biology Datasets for Students

[![License: CC0](https://img.shields.io/badge/License-CC0%201.0-lightgrey.svg)](http://creativecommons.org/publicdomain/zero/1.0/)
[![Auto Update Status](https://github.com/umeshtharukaofficial/bio-datasets-1M/actions/workflows/auto-update.yml/badge.svg)](https://github.com/umeshtharukaofficial/bio-datasets-1M/actions)

Welcome to **Bio-Datasets-1M**, an open, growing public repository containing **1,000,000 individual biology datasets** specifically created for students, educators, and researchers worldwide. 

The collection is automatically expanded every **5 minutes** by an autonomous bot, with a goal of reaching one million unique dataset files across various fields of biological sciences.

## 🤗 Also on HuggingFace

Mirror updated every 5 minutes:
https://huggingface.co/datasets/umeshtharukaofficial/bio-datasets-1M

Load a random dataset in 3 lines:
```python
from huggingface_hub import hf_hub_download
import pandas as pd
df = pd.read_csv(hf_hub_download("umeshtharukaofficial/bio-datasets-1M",
                                 "datasets/genomics/genomics_000001_variant.csv",
                                 repo_type="dataset"))
```

---

## 📂 Category Folder Guide

Each dataset is stored as a separate `.csv` file inside its respective category directory under `datasets/`. Here is what each category contains:

| Category | Description / Schema Fields |
| :--- | :--- |
| **`genomics`** | DNA sequence variants. Fields: `sample_id`, `chromosome`, `position`, `ref_allele`, `alt_allele`, `gene`, `quality` |
| **`proteomics`** | Protein sequences and physical properties. Fields: `protein_id`, `sequence`, `length`, `mass_da`, `isoelectric_point`, `organism` |
| **`ecology`** | Field observation and population samples. Fields: `species`, `latitude`, `longitude`, `population`, `date`, `habitat` |
| **`microbiology`** | Bacterial strains and culture observations. Fields: `strain_id`, `genus`, `species`, `gram_stain`, `oxygen_req`, `colony_diameter_mm` |
| **`botany`** | Plant species phenotypes. Fields: `species`, `family`, `leaf_length_cm`, `flower_color`, `habitat`, `region` |
| **`zoology`** | Animal species classifications and measurements. Fields: `species`, `class`, `order`, `weight_kg`, `length_cm`, `conservation_status` |
| **`cell-biology`** | Cellular structure and viability. Fields: `cell_id`, `cell_type`, `diameter_um`, `organelle_count`, `viability_pct` |
| **`neuroscience`** | Neuronal electrophysiology recording simulations. Fields: `neuron_id`, `region`, `firing_rate_hz`, `spike_amplitude_mv`, `subject_species` |
| **`biochemistry`** | Biochemical compound profiles. Fields: `compound`, `formula`, `mw`, `pka`, `solubility_mg_ml`, `class` |
| **`bioinformatics`** | Sequence analysis parameters. Fields: `sequence_id`, `sequence`, `length`, `gc_content`, `source_organism` |

---

## ⚡ How to Get the Data

### 1. Download a Single File
Simply browse to any file in GitHub, click on it, and click **Raw** -> Right-click and choose **Save As...** or copy the URL.

### 2. Download a Single Category Folder
To avoid cloning the entire 1M dataset repo (which can become extremely large), you can use Git sparse checkout:

```bash
git clone --no-checkout https://github.com/umeshtharukaofficial/bio-datasets-1M.git
cd bio-datasets-1M
git sparse-checkout set datasets/genomics
git checkout
```

### 3. Clone the Entire Repository
```bash
git clone https://github.com/umeshtharukaofficial/bio-datasets-1M.git
```

---

## 🐍 How to Load in Python

You can easily read any dataset using `pandas`:

```python
import pandas as pd

# Load genomic variant dataset
df = pd.read_csv("datasets/genomics/genomics_1_a2b3c4.csv")
print(df.head())
```

---

## 📈 Manifest & Progress

All generated datasets are cataloged in [manifest/index.csv](file:///home/Asus/bio-datasets-1M/manifest/index.csv). You can check this file to get the full list of files, sizes, and row counts.

---

## ⚖️ License

This repository is dedicated to the public domain under the [Creative Commons Zero (CC0-1.0) License](LICENSE). You are free to copy, modify, distribute, and perform the work, even for commercial purposes, all without asking permission.

---

## ⚠️ Disclaimer & Contribution

> [!WARNING]
> All data in this repository is **synthetically generated** for educational, practice, and learning purposes only. It does **not** represent real clinical, medical, or biological study outcomes. Do not use this data for actual diagnostic or clinical decision-making.

For feedback, issues, or suggestions, please open a GitHub issue on the repository [Issues Page](https://github.com/umeshtharukaofficial/bio-datasets-1M/issues).
