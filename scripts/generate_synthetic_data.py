import pandas as pd
import numpy as np

# ============================================================
# STEP 1 — Extract real stats from both Kaggle datasets
# ============================================================

upi_df = pd.read_csv('../data/raw/upi_transactions_2024.csv')
wallet_df = pd.read_csv('../data/raw/digital_wallet_transactions.csv')

# --- Amount stats ---
upi_amounts = upi_df['amount (INR)']
wallet_amounts = wallet_df['product_amount']

upi_amounts = upi_amounts[(upi_amounts > 0) & (upi_amounts <= 5000)]
wallet_amounts = wallet_amounts[(wallet_amounts > 0) & (wallet_amounts <= 5000)]

combined_amounts = pd.concat([upi_amounts, wallet_amounts])

real_mean = combined_amounts.mean()
real_std = combined_amounts.std()

print(f"Real combined amount mean: {real_mean:.2f}, std: {real_std:.2f}")

# --- Daily transaction volume ---
upi_df['date'] = pd.to_datetime(upi_df['timestamp']).dt.date
wallet_df['date'] = pd.to_datetime(wallet_df['transaction_date']).dt.date

upi_daily_avg = upi_df.groupby('date').size().mean()
wallet_daily_avg = wallet_df.groupby('date').size().mean()

print(f"UPI avg txns/day: {upi_daily_avg:.1f}")
print(f"Wallet avg txns/day: {wallet_daily_avg:.1f}")

# --- Day-of-week pattern (weekend vs weekday) ---
def day_name(d):
    return pd.Timestamp(d).day_name()

upi_df['day_name'] = upi_df['date'].apply(day_name)
weekend_days = ['Saturday', 'Sunday']

upi_weekend_avg = upi_df[upi_df['day_name'].isin(weekend_days)].groupby('date').size().mean()
upi_weekday_avg = upi_df[~upi_df['day_name'].isin(weekend_days)].groupby('date').size().mean()

weekend_factor = upi_weekend_avg / upi_weekday_avg if upi_weekday_avg > 0 else 1.2
print(f"Weekend factor (relative to weekday): {weekend_factor:.2f}")


# ============================================================
# STEP 2 — Generate synthetic data calibrated to those stats
# ============================================================

np.random.seed(42)

date_range = pd.date_range('2023-09-01', '2024-12-31', freq='D')

# use the smaller of the two real daily averages as a baseline
# (keeps volume realistic for a small merchant, not inflated)
base_daily_txns = min(upi_daily_avg, wallet_daily_avg, 20)

# derive lognormal parameters from real mean/std
# (lognormal mean of underlying normal ≈ ln(mean^2 / sqrt(std^2 + mean^2)))
sigma = np.sqrt(np.log(1 + (real_std ** 2) / (real_mean ** 2)))
mu = np.log(real_mean) - (sigma ** 2) / 2

print(f"Derived lognormal params -> mu: {mu:.3f}, sigma: {sigma:.3f}")

records = []

for date in date_range:
    is_weekend = date.dayofweek in [5, 6]
    day_factor = weekend_factor if is_weekend else 1.0

    # mild upward growth trend across the full date range
    progress = (date - date_range[0]).days / len(date_range)
    growth_factor = 1 + progress * 0.4

    # occasional spike days (festivals, promotions)
    spike_factor = 2.5 if np.random.rand() < 0.02 else 1.0

    expected_txns = base_daily_txns * day_factor * growth_factor * spike_factor
    n_txns = int(np.random.poisson(expected_txns))

    for _ in range(n_txns):
        amount = np.random.lognormal(mean=mu, sigma=sigma)
        amount = min(round(amount, 2), 5000)

        # random time within the day
        hour = np.random.randint(0, 24)
        minute = np.random.randint(0, 60)
        timestamp = pd.Timestamp(date) + pd.Timedelta(hours=hour, minutes=minute)

        records.append({
            'timestamp': timestamp,
            'amount': amount,
            'day_of_week': timestamp.day_name(),
            'transaction_type': 'P2M',
            'source': 'synthetic'
        })

synthetic_df = pd.DataFrame(records)
synthetic_df['transaction_id'] = ['S' + str(i) for i in range(len(synthetic_df))]

# reorder columns to match your existing schema
final_cols = ['transaction_id', 'timestamp', 'transaction_type', 'amount', 'day_of_week', 'source']
synthetic_df = synthetic_df[final_cols]
synthetic_df = synthetic_df.sort_values('timestamp').reset_index(drop=True)

# ============================================================
# STEP 3 — Sanity checks before saving
# ============================================================

print("\nFinal dataset shape:", synthetic_df.shape)
print(synthetic_df['amount'].describe())
print("\nAvg transactions/day:", synthetic_df.groupby(synthetic_df['timestamp'].dt.date).size().mean())

# ============================================================
# STEP 4 — Save as your new unified dataset
# ============================================================

synthetic_df.to_csv('../data/processed/unified_transactions.csv', index=False)
print("\nSaved to ../data/processed/unified_transactions.csv")