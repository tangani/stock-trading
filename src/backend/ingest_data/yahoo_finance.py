from sqlalchemy import create_engine
import pandas as pd
import psycopg2
import io
import yfinance as yf


companies = ["TSLA", "PLTR", "AMD", "AMZN", "SOFI", "NIO", "AAPL", "GOOGL", "PBR", "UBER", "SWN"]

df = pd.DataFrame()

for stock in companies:
    ticker = yf.Ticker(stock)
    stock_history = ticker.history(period="30mo")
    stock_history["company"] = stock
    # df = df.append(stock_history)

    # resp = requests.post(f"{BASE_ENDPOINT}{INGEST_ENDPOINT}", json=request_body)
    df = pd.concat([df, stock_history])

# psql -U postgres -h 127.0.0.1 -d postgres
engine = create_engine(
    'postgresql+psycopg2://postgres:5432@localhost:5432/postgres')

# Drop old table and create new empty table
df.head(0).to_sql('yahoo_finance', engine, if_exists='replace',index=False)

conn = engine.raw_connection()
cur = conn.cursor()
output = io.StringIO()
df.to_csv(output, sep='\t', header=False, index=False)
output.seek(0)
contents = output.getvalue()
cur.copy_from(output, 'yahoo_finance', null="") # null values become ''
conn.commit()
cur.close()
conn.close()