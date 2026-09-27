from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

app = FastAPI()

# Allow the React dev server to call this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite's default port
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/transactions")
def get_transactions():
    df = pd.read_csv("../data/processed/unified_transactions.csv")
    # limit rows for now — no one needs 50k rows in a raw table view
    df = df.head(100)
    return df.to_dict(orient="records")

@app.get("/api/sales-trend")
def get_sales_trend():
    df = pd.read_csv("../data/processed/unified_transactions.csv")
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    df['date'] = df['timestamp'].dt.date

    # aggregate total sales per day
    daily_sales = df.groupby('date')['amount'].sum().reset_index()
    daily_sales.columns = ['date', 'total_sales']
    daily_sales = daily_sales.sort_values('date')

    # convert date to string so it's JSON-serializable
    daily_sales['date'] = daily_sales['date'].astype(str)

    return daily_sales.to_dict(orient='records')