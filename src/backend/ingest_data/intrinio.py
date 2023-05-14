"""
TODO: There is no active subscription on this platform yet and the API key does not have permissions

Documentation: https://docs.intrinio.com/documentation/python

requirements: pip install intrinio-sdk

api_key: OjliNDk2NDAzNDI4NDZjNWVhYTc0NjhiYTRjN2EzYWFh
"""

from __future__ import print_function
import time
import intrinio_sdk as intrinio
from intrinio_sdk.rest import ApiException

api_key = "OjliNDk2NDAzNDI4NDZjNWVhYTc0NjhiYTRjN2EzYWFh"
company = "AAPL"

intrinio.ApiClient().set_api_key(api_key)
intrinio.ApiClient().allow_retries(True)

identifier =company
start_date = '2018-01-01'
end_date = '2019-01-01'
frequency = 'daily'
page_size = 100
next_page = ''

response = intrinio.SecurityApi().get_security_stock_prices(identifier, start_date=start_date, end_date=end_date,
                                                            frequency=frequency, page_size=page_size, next_page=next_page)
print(response)