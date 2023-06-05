import streamlit as st
import pandas as pd
import yfinance as yf

# Title of the app
st.title("Finance Dashboard")

# Tickers of the stocks to be displayed
tickers = ['BTC-USD', 'ETH-USD', 'LTC-USD',
           'DOGE-USD', 'AAPL-USD', 'AMZN-USD', 'MSFT-USD']

# Dropdown menu
dropdown = st.multiselect("Pick your Asset", tickers)

# Start and End date
startdate = st.date_input("Start Date", value=pd.to_datetime("2021-01-01"))
enddate = st.date_input("End Date", value=pd.to_datetime("2023-05-31"))

# Function for cumulative returns
def relative_returns(df):
    rel = df.pct_change()
    cumret = (1 + rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


# Pull data from yfinance
if len(dropdown) > 0:
    # df = yf.download(dropdown, startdate, enddate)['Adj Close']
    df = relative_returns(yf.download(dropdown, startdate, enddate))['Adj Close']
    st.line_chart(df)