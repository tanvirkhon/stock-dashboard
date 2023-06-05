import streamlit as st
import pandas as pd
import yfinance as yf

# Title of the app
st.title("Finance Dashboard")

# Tickers of the stocks to be displayed
tickers = ['BTC-USD', 'ETH-USD', 'LTC-USD',
           'DOGE-USD', 'AAPL-USD', 'AMZN-USD', 'MSFT-USD']


dropdown = st.multiselect("Pick your Asset", tickers)
