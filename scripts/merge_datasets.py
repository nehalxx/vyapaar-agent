import pandas as pd
from pathlib import Path

# ---- Resolve paths relative to this script's location ----
SCRIPT_DIR = Path(__file__).resolve().parent      # .../vyapaar-agent/scripts
ROOT_DIR = SCRIPT_DIR.parent                        # .../vyapaar-agent
RAW_DIR = ROOT_DIR / 'data' / 'raw'
PROCESSED_DIR = ROOT_DIR / 'data' / 'processed'

# ---- Load both CSVs ----
upi_df = pd.read_csv(RAW_DIR / 'upi_transactions_2024.csv')
wallet_df = pd.read_csv(RAW_DIR / 'digital_wallet_transactions.csv')

# ---- 1. UPI dataset: select and rename what you need ----
upi_clean = upi_df[[
    'transaction id', 'timestamp', 'transaction type',
    'amount (INR)', 'day_of_week'
]].copy()

upi_clean.columns = ['transaction_id', 'timestamp', 'transaction_type', 'amount', 'day_of_week']

# regenerate clean IDs, tag source
upi_clean['transaction_id'] = 'U' + upi_clean.index.astype(str)
upi_clean['source'] = 'upi'

# ---- 2. Wallet dataset: select and rename what you need ----
wallet_clean = wallet_df[[
    'transaction_id', 'transaction_date', 'product_amount'
]].copy()

wallet_clean.columns = ['transaction_id', 'timestamp', 'amount']

# derive day_of_week from the real date — no assumptions needed
wallet_clean['timestamp'] = pd.to_datetime(wallet_clean['timestamp'])
wallet_clean['day_of_week'] = wallet_clean['timestamp'].dt.day_name()

# every wallet transaction is a merchant payment
wallet_clean['transaction_type'] = 'P2M'

# regenerate clean IDs, tag source
wallet_clean['transaction_id'] = 'W' + wallet_clean.index.astype(str)
wallet_clean['source'] = 'wallet'

# ---- 3. Filter amounts to your target range (0–5000) ----
upi_clean = upi_clean[(upi_clean['amount'] > 0) & (upi_clean['amount'] <= 5000)]
wallet_clean = wallet_clean[(wallet_clean['amount'] > 0) & (wallet_clean['amount'] <= 5000)]

# ---- 4. Make sure timestamp formats match before merging ----
upi_clean['timestamp'] = pd.to_datetime(upi_clean['timestamp'])

# ---- 5. Merge into one unified dataset ----
final_cols = ['transaction_id', 'timestamp', 'transaction_type', 'amount', 'day_of_week', 'source']
unified_df = pd.concat([upi_clean[final_cols], wallet_clean[final_cols]], ignore_index=True)

# sort chronologically
unified_df = unified_df.sort_values('timestamp').reset_index(drop=True)

# ---- 6. Sanity checks before saving ----
print(unified_df.shape)
print(unified_df['amount'].describe())
print(unified_df['source'].value_counts())
unified_df['amount'].hist(bins=50)  # visually confirm the skew looks realistic

# ---- 7. Save ----
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)  # in case it doesn't exist yet
unified_df.to_csv(PROCESSED_DIR / 'unified_transactions.csv', index=False)