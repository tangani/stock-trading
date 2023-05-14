FROM python:3.8-slim

WORKDIR /app

RUN apt-get update && apt-get install -y build-essential libpq-dev

COPY .requirements/dev.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./src/data_store/backend/ingest_data/yahoo_finance.py /app/data_store

EXPOSE 8000

CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "data_store.main:app", "-b", "0.0.0.0:8000", "--timeout", "600"]