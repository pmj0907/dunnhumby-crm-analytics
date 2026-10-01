
# %%
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_DIR = PROJECT_ROOT / "data" / "raw"

# %%
# 1. campaign_desc의 CAMPAIGN 유일성 확인

campaign_desc = pd.read_csv(RAW_DATA_DIR / "campaign_desc.csv")

print("[campaign_Desc]")
print("행 수:", len(campaign_desc))
print("CAMPAIGN 고유값 수 :", campaign_desc["CAMPAIGN"].nunique())
print("CAMPAIGN 중복 수 :", campaign_desc["CAMPAIGN"].duplicated().sum())

# %%
# 2. campaign_table의 household_key 유일성 확인

campaign_table = pd.read_csv(RAW_DATA_DIR / "campaign_table.csv")

print("\n[campaign_table]")
print("행 수: ", len(campaign_table))
print("household_key 고유값 수 :", campaign_table["household_key"].nunique())
print("household_key 중복 수 :", campaign_table["household_key"].duplicated().sum())

print("CAMPAIGN 고유값 수 :", campaign_table["CAMPAIGN"].nunique())
print("CAMPAIGN 중복 수 :", campaign_table["CAMPAIGN"].duplicated().sum())

# %%
# 3. campaign_table의 household_key + CAMPAIGN 조합의 유일성 확인
duplicate_pairs = campaign_table.duplicated(subset=["household_key", "CAMPAIGN"]).sum()

print("household_key + CAMPAIGN 중복 수 :", duplicate_pairs)

# %%
# 4. hh_demographic의 household_key 유일성 확인
hh_demo = pd.read_csv(RAW_DATA_DIR / "hh_demographic.csv")

print("\n[hh_demographic]")
print("행 수:", len(hh_demo))
print("household_key 고유값 수:", hh_demo["household_key"].nunique())
print("household_key 중복 수:", hh_demo["household_key"].duplicated().sum())

# %%
# 5. transaction_data의 주요 키 후보 확인
transaction = pd.read_csv(RAW_DATA_DIR / "transaction_data.csv")

print("\n[transaction_data]")
print("행 수:", len(transaction))
print("household_key 고유값 수:", transaction["household_key"].nunique())
print("BASKET_ID 고유값 수:", transaction["BASKET_ID"].nunique())
print("PRODUCT_ID 고유값 수:", transaction["PRODUCT_ID"].nunique())

print("BASKET_ID 중복 수:", transaction["BASKET_ID"].duplicated().sum())

print(
    "BASKET_ID + PRODUCT_ID 중복 수:",
    transaction.duplicated(subset=["BASKET_ID", "PRODUCT_ID"]).sum(),
)


# transaction_data 중 demographic이 없는 household_key 개수 확인
# set() : 중복을 제거한 집합

transaction_households = set(transaction["household_key"])
demographic_households = set(hh_demo["household_key"])

only_in_transaction = transaction_households - demographic_households
only_in_demographic = demographic_households - transaction_households

print("\n[household_key 포함관계]")
print("transaction에만 있는 household 수 :", len(only_in_transaction))
print("demographic에만 있는 household 수 :", len(only_in_demographic))

# %%
# 6. product의 PRODUCT_ID 유일성 확인
product = pd.read_csv(RAW_DATA_DIR / "product.csv")

print("\n[product]")
print("행 수:", len(product))
print("PRODUCT_ID 고유값 수:", product["PRODUCT_ID"].nunique())
print("PRODUCT_ID 중복 수:", product["PRODUCT_ID"].duplicated().sum())

# PRODUCT_ID 포함관계
transaction_products = set(transaction["PRODUCT_ID"])
product_master_ids = set(product["PRODUCT_ID"])

only_in_transaction_product = transaction_products - product_master_ids
only_in_product_master = product_master_ids - transaction_products

print("\n[PRODUCT_ID 포함관계]")
print("transaction에만 있는 PRODUCT_ID 수:", len(only_in_transaction_product))
print("product에만 있는 PRODUCT_ID 수:", len(only_in_product_master))

# %%
# coupon, coupon_redempt, causal_data 확인
coupon = pd.read_csv(RAW_DATA_DIR / "coupon.csv")
coupon_redempt = pd.read_csv(RAW_DATA_DIR / "coupon_redempt.csv")
causal = pd.read_csv(RAW_DATA_DIR / "causal_data.csv")

print("\n[coupon]")
print("행 수:", len(coupon))
print("COUPON_UPC 고유값 수:", coupon["COUPON_UPC"].nunique())
print("COUPON_UPC 중복 수:", coupon["COUPON_UPC"].duplicated().sum())
print(
    "COUPON_UPC + PRODUCT_ID + CAMPAIGN 중복 수:",
    coupon.duplicated(subset=["COUPON_UPC", "PRODUCT_ID", "CAMPAIGN"]).sum(),
)

print("\n[coupon_redempt]")
print("행 수:", len(coupon_redempt))
print(
    "household_key + COUPON_UPC + CAMPAIGN 중복 수:",
    coupon_redempt.duplicated(subset=["household_key", "COUPON_UPC", "CAMPAIGN"]).sum(),
)
print(
    "household_key + DAY + COUPON_UPC + CAMPAIGN 중복 수:",
    coupon_redempt.duplicated(
        subset=["household_key", "DAY", "COUPON_UPC", "CAMPAIGN"]
    ).sum(),
)

print("\n[causal_data]")
print("행 수:", len(causal))
print(
    "PRODUCT_ID + STORE_ID + WEEK_NO 중복 수:",
    causal.duplicated(subset=["PRODUCT_ID", "STORE_ID", "WEEK_NO"]).sum(),
)
print(
    "PRODUCT_ID + STORE_ID + WEEK_NO + display + mailer 중복 수:",
    causal.duplicated(
        subset=["PRODUCT_ID", "STORE_ID", "WEEK_NO", "display", "mailer"]
    ).sum(),
)

print("\n[완전 동일 행 중복 확인]")

print("coupon 전체 행 기준 중복 수:", coupon.duplicated().sum())

print("coupon_redempt 전체 행 기준 중복 수:", coupon_redempt.duplicated().sum())

print("causal_data 전체 행 기준 중복 수:", causal.duplicated().sum())

# %%
duplicate_causal = causal[
    causal.duplicated(
        subset=["PRODUCT_ID", "STORE_ID", "WEEK_NO"],
        keep=False
    )
].sort_values(
    ["PRODUCT_ID", "STORE_ID", "WEEK_NO"]
)

print("\n[causal_data 중복 사례]")
print(duplicate_causal.head(20))
# %%
