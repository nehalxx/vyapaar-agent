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

- **Sales trend visualization** — line graph of sales over time
- **Low vs. high sales days** — filterable by week/month/year, sorted
- **Cash flow forecasting** — linear regression (built from scratch, no inbuilt ML
  libraries)
- **Rent & bill tracking with reminders** — rule-based due-date monitoring
- **Peak/off-peak sales hours** — k-means clustering (built from scratch)
- **Discount suggestions** — statistical thresholds + business rules based on average
  purchase behavior
- **Safe spend estimate** — combines forecasted inflow, known fixed costs, and a buffer
  to flag safe discretionary spend

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

[Add team member names here]
