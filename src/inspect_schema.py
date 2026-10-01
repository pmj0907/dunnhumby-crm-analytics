
from pathlib import Path

import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

files = [
    "hh_demographic.csv",
    "transaction_data.csv",
    "campaign_desc.csv",
    "campaign_table.csv",
    "product.csv",
    "coupon.csv",
    "coupon_redempt.csv",
    "causal_data.csv",
]

for file_name in files:
    file_path = RAW_DATA_DIR / file_name

    # nrows = 0 : 데이터는 읽지 않고 컬럼만 확인
    df = pd.read_csv(file_path, nrows=0)

    print(f"\n[{file_name}]")
    print(df.columns.tolist())

# %%
