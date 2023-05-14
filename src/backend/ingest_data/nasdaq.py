"""
Documentation: https://github.com/Nasdaq/data-link-python/#local-api-key-environment-variable

requirements: pip install Nasdaq-Data-Link

api_key: 5s5heDHY4xbphsJ5eszu
"""

import nasdaqdatalink
import pandas as pd

api_key = "5s5heDHY4xbphsJ5eszu"

company = "AAPL"

data = nasdaqdatalink.get_table('ZACKS/FC', ticker=f'{company}')

print(type(data))
print(data.head())
# data.to_csv("testing.csv")
print(data.shape)
