from pathlib import Path

import kagglehub

# parents[0] : src, parents[1] : dunnhumby-crm-analytics - root folder
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

RAW_DATA_DIR.mkdir(parents=True, exist_ok=True)

dataset_path = kagglehub.dataset_download(
    "frtgnn/dunnhumby-the-complete-journey",
    output_dir=str(RAW_DATA_DIR),
)

print(f"Dataset downloaded to: {dataset_path}")
