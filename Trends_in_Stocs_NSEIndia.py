from nsepy import  get_history
from datetime import date
import streamlit as st
import pandas as pd

#https://github.com/swapniljariwala/nsepy

list_of_stocks = [
    'SBIN',
    'TATASTEEL',
    'DIVISLAB',
    'KOTAKBANK',
    'DRREDDY',
    'ULTRACEMCO',
    'RELIANCE'
    ]
nseSymbol = st.radio('Select a stock', list_of_stocks)
st.write("""
# Stock Price App
""")
st.subheader(f'Stock Price of {nseSymbol} for the last 10 years')
startDate = st.date_input('Enter Starting Date(YYYY-MM-DD):')
endDate = st.date_input('Enter End Date(YYYY-MM-DD):')
data = get_history(symbol=nseSymbol,start = startDate, end=endDate)
st.line_chart(data[['Close']])
