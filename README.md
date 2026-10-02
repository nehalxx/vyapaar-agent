# Vyapaar Agent

An AI agent that turns merchant transaction data into proactive growth insights and
actions — not a chatbot that answers questions, but a system that detects patterns and
acts on them.

## Problem

Small and mid-sized merchants have access to their own payment data, but no
intelligence layer on top of it — no proactive insights, no automated actions to help
them grow or manage cash flow. The data exists, but nothing turns it into decisions.

## What This Is

An AI agent built entirely on transaction-level data (amount, timestamp, day/time) —
no assumptions about inventory or item-level data that merchants would need to provide
separately. Thresholds and suggestions are computed **relative to each merchant's own
baseline**, so the same logic works for a small kirana store and a larger retailer
alike, without needing separate models.

## Features

- **Sales trend visualization** — line graph of sales over time to show whether the
  business is growing, flat, or declining
- **Low vs. high sales days** — ranks days by sales volume (filterable by week/month/
  year) so merchants can spot and act on weak periods
- **Cash flow forecasting** — predicts expected future inflow using a from-scratch
  linear regression model on time-based sales patterns
- **Rent & bill tracking with reminders** — tracks recurring expenses and proactively
  reminds merchants before due dates
- **Peak/off-peak sales hours** — from-scratch k-means clustering to identify natural
  high- and low-activity time windows during the day
- **Discount suggestions** — a personalized discount threshold based on the merchant's
  own typical purchase size, not a fixed amount
- **Safe spend estimate** — combines forecasted inflow, known bills, and a safety
  buffer into one clear "safe to spend" number

## Tech Stack

- **Backend:** FastAPI
- **Database:** CSV-based data pipeline (raw → processed)
- **Frontend:** React (Vite) + Recharts
- **Core logic:** numpy / pandas for data handling; hand-built linear regression and
  k-means clustering (no inbuilt ML libraries, per competition constraints); rule-based
  logic for reminders and discount/spend suggestions

## Dataset

Initial transaction data was derived from two public Kaggle datasets — UPI
Transactions 2024 and Digital Wallet Transactions. Merging the two directly revealed a
scale and density mismatch between the 2023 and 2024 sources (very different
transaction volumes and amount ranges), so a synthetic data generator was built
instead, calibrated against the real datasets' amount distribution and per-weekday
transaction patterns. This produces consistent daily coverage with realistic seasonal
variation while staying grounded in real-world statistics.

- `scripts/merge_datasets.py` — initial direct-merge attempt (kept for reference/
  provenance; not used in the final pipeline)
- `scripts/generate_synthetic_data.py` — produces the dataset actually used by the app

## Why No Inbuilt ML Libraries

Core ML algorithms (regression, clustering) are implemented from scratch using numpy
rather than libraries like scikit-learn, to demonstrate a working understanding of the
underlying methods.

## Project Structure
vyapaar-agent/
├── data/
│ ├── raw/ # original Kaggle CSVs
│ └── processed/ # unified, synthetic transaction dataset
├── scripts/ # data generation/prep scripts
├── backend/ # FastAPI app
└── frontend/ # React (Vite) app


## Status

🚧 In development — built in phases, starting from a basic data pipeline through to
full feature set.

**Completed:**
- Phase 0: end-to-end pipeline (CSV → FastAPI → React table)
- Phase 1: sales trend line graph
- Phase 2: low vs. high sales days (filterable by day/month/year)

**In progress:** bill reminders, forecasting, clustering, discount logic, safe spend
estimate.

## By
Ilisha Shah and Nehal Katlana
