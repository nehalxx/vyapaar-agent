# vyapaar-agent — AI Growth Partner for Paytm Merchants

Built for the Paytm Build for India AI Hackathon – Mumbai Edition (Track 1: Merchant Growth AI)

## Problem

Paytm merchants get payment processing, but no intelligence layer on top of it. Payment
data exists, but there's nothing turning it into decisions — no proactive insights, no
automated actions to help merchants grow or manage cash flow.

## What This Is

An AI agent — not a chatbot — that analyzes merchant transaction data and takes or
proposes concrete actions, rather than just answering questions. It runs entirely on
transaction-level data (amount, timestamp, customer ID/repeat status), which is what
Paytm actually has access to — no assumptions about inventory or item-level data that
merchants would need to provide separately.

## Features

- **Sales trend visualization** — Line graph of sales over time to show whether the business is growing, flat, or declining.
- **Low vs. high sales days** — Ranks days by sales volume (filterable by week/month/year) so merchants can spot and act on weak days.
-** Cash flow forecasting** — Predicts expected future inflow using a from-scratch linear regression model on time-based sales patterns.
-** Rent & bill tracking with reminders **— Tracks recurring expenses and proactively reminds merchants before due dates.
- **Peak/off-peak sales hours** — Uses from-scratch k-means clustering to identify natural high- and low-activity time windows during the day.
-** Discount suggestions** — Recommends a personalized discount threshold based on the merchant's own typical purchase size, not a fixed amount.
- **Safe spend estimate** — Combines forecasted inflow, known bills, and a safety buffer into one clear "safe to spend" number.

## Tech Stack

- **Backend:** FastAPI
- **Database:** SQLite (`transactions` table — synthetic/sample data for demo purposes)
- **Frontend:** React (Vite) + Recharts
- **Core logic:** numpy / pandas for data handling; hand-built linear regression and
  k-means clustering (no inbuilt ML libraries, per hackathon constraints); rule-based
  logic for reminders and discount/spend suggestions

## Why No Inbuilt ML Libraries

Per hackathon guidelines, core ML algorithms (regression, clustering) are implemented
from scratch using numpy rather than libraries like scikit-learn, to demonstrate a
working understanding of the underlying methods.

## Status

🚧 In development — built in phases, starting from a basic data pipeline through to
full feature set. See project roadmap for build order.

## Team

Nehal katlana
Ilisha shah
