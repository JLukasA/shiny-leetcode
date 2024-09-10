from datetime import datetime
import datetime
import pandas as pd
import sqlite3
import sqlalchemy
import yfinance as yf


# Select tickers and time range for extraction, and extract into dataframe using yfinance
tickers = ['NVDA', 'MSFT', 'AAPL', 'NFLX', 'GOOG']
end_date = datetime.datetime.now()
start_date = end_date - datetime.timedelta(days=1)

df = pd.DataFrame()
for ticker in tickers:
    stock = yf.Ticker(ticker)
    stock_data = stock.history(start=start_date, end=end_date, interval="15m")
    stock_data['symbol'] = ticker
    df = pd.concat([df, stock_data])

# Clean
df = df.reset_index()
df = df.drop(['Dividends', 'Stock Splits', 'High', 'Low', ], axis=1)
