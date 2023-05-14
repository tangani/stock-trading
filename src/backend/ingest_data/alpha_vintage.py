"""
Documentation: https://www.alphavantage.co/documentation/
access key: KU54O7U7WWGCACXT

This script is for IBM

The advantage with this API is we get 5 minutes intervals of the stock price vs the Yahoo finance which
    returns end of day stock prices

Available data:
    * Core Time Series Stock Data APIs
    * Alpha Intelligence
    * Fundamental Data
    * Physical and Digital/Crypto Currencies (e.g., Bitcoin)
    * Commodities
    * Economic Indicators
    * Technical Indicators
"""

import requests

company = "IBM"
api_key = "KU54O7U7WWGCACXT"

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={company}&interval=5min&apikey={api_key}'
r = requests.get(url)
data = r.json()

print(data)