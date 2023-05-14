import httpx
import yfinance as yf

import os

CONNECT_API_HOST = os.environ.get("CONNECT_API_HOST", "localhost")
CONNECT_API_PORT = os.environ.get("CONNECT_API_PORT", "9991")
BASE_ENDPOINT = f"http://{CONNECT_API_HOST}:{CONNECT_API_PORT}"

companies = ["TSLA", "PLTR", "AMD", "AMZN", "SOFI", "NIO", "AAPL", "GOOGL", "PBR", "UBER", "SWN"]

# 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

for stock in companies:
    ticker = yf.Ticker(stock)
    stock_history = ticker.history(period="1mo")
    stock_history["company"] = stock
    print(stock_history.shape)
    print(stock_history.head())

    # resp = requests.post(f"{BASE_ENDPOINT}{INGEST_ENDPOINT}", json=request_body)
    break
