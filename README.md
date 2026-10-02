# Vyapaar Agent — AI Growth Partner for Paytm Merchants

Built for the Paytm Build for India AI Hackathon – Mumbai Edition (Track 1: Merchant Growth AI)
Team: enTropy

## Problem

Paytm merchants get payment processing, but no intelligence layer on top of it. Payment
data exists, but there's nothing turning it into decisions — no proactive insights, no
automated actions to help merchants grow or manage cash flow.

## What This Is

An AI agent — not a chatbot — that analyzes merchant transaction data and takes or
proposes concrete actions, rather than just answering questions. It runs entirely on
transaction-level data (amount, timestamp, day/time, customer/repeat status), which is
what Paytm actually has access to — no assumptions about inventory or item-level data
that merchants would need to provide separately. Thresholds and suggestions are computed
relative to each merchant's own baseline, so the same logic scales from a small kirana
store to a larger retail merchant without needing separate models.

## Features

- **Sales trend visualization** — Line graph of sales over time to show whether the
  business is growing, flat, or declining.
- **Low vs. high sales days** — Ranks days by sales volume (filterable by day-of-week/
  month/year) so merchants can spot and act on weak periods.
- **Cash flow forecasting** — Predicts expected future inflow using a from-scratch
  linear regression model on time-based sales patterns.
- **Rent & bill tracking with reminders** — Tracks recurring expenses and proactively
  reminds merchants before due dates.
- **Peak/off-peak sales hours** — Uses from-scratch k-means clustering to identify
  natural high- and low-activity time windows during the day.
- **Discount suggestions** — Recommends a personalized discount threshold based on the
  merchant's own typical purchase size, not a fixed amount.
- **Safe spend estimate** — Combines forecasted inflow, known bills, and a safety
  buffer into one clear "safe to spend" number.

## Tech Stack

- **Backend:** FastAPI
- **Database/storage:** CSV-based pipeline (raw → processed); SQLite planned
- **Frontend:** React (Vite) + Recharts
- **Core logic:** numpy / pandas for data handling; hand-built linear regression and
  k-means clustering (no inbuilt ML libraries, per hackathon constraints); rule-based
  logic for reminders and discount/spend suggestions

## Why No Inbuilt ML Libraries

Per hackathon guidelines, core ML algorithms (regression, clustering) are implemented
from scratch using numpy rather than libraries like scikit-learn, to demonstrate a
working understanding of the underlying methods.

## Dataset

Dataset derived from Kaggle's **UPI Transactions 2024** and **Digital Wallet
Transactions** datasets. Directly merging the two raw datasets revealed a scale and
density mismatch between 2023 and 2024-sourced data (see `scripts/merge_datasets.py`,
kept for reference/provenance — superseded, not used in the final pipeline).

Real transaction amount distributions and per-weekday volume patterns were extracted
from both sources and used to calibrate a synthetic data generator
(`scripts/generate_synthetic_data.py`), producing consistent daily coverage with
realistic weekly seasonality, a gradual growth trend, and occasional spike days. This
is the script that produces the dataset actually used by the app
(`data/processed/unified_transactions.csv`).

## Project Structure
