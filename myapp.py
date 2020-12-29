#!/usr/bin/env python
# coding: utf-8

# In[2]:


import yfinance as yf
import streamlit as st


# In[3]:


st.write("""
# Simple Stock Price App
Shown are the stock closing price and volume of Google!
""")


# In[4]:


# https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
#define the ticker symbol
tickerSymbol = 'GOOGL'


# In[5]:


#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)


# In[6]:


#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')


# In[7]:


st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)





