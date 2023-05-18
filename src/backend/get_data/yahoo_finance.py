import psycopg2
from sqlalchemy import create_engine
import pandas as pd

def get_data(table):
    
    engine = create_engine(
    'postgresql+psycopg2://postgres:5432@localhost:5432/postgres')

    df = pd.read_sql(f"select * from {table}", con=engine)

    return df


if __name__ == "__main__":
    get_data("yahoo_finance")

