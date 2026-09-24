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