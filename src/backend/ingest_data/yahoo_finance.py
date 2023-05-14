import httpx
import yfinance as yf

companies = ["TSLA", "PLTR", "AMD", "AMZN", "SOFI", "NIO", "AAPL", "GOOGL", "PBR", "UBER", "SWN"]

# 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

for stock in companies:
    ticker = yf.Ticker(stock)
    stock_history = ticker.history(period="1mo")
    print(stock_history.shape)
    print(stock_history.head())

