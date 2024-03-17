# filename: stock_chart.py

import pandas as pd
import matplotlib.pyplot as plt

# Download historical stock prices from Yahoo Finance using Pandas-datareader library
import yfinance as yf

def download_data(symbol, start, end):
    df = yf.download(symbol, start, end)
    return df['Adj Close']

NVDA = download_data('NVDA', '2022-01-01', '2022-07-15')
TESLA = download_data('TSLA', '2022-01-01', '2022-07-15')

# Calculate Year-to-Date percentage change
NVDA_YTD = NVDA.iloc[-1]/NVDA.iloc[0] - 1
TESLA_YTD = TESLA.iloc[-1]/TESLA.iloc[0] - 1

# Plot the charts with labels and legends
plt.figure(figsize=(12, 6))
plt.plot(NVDA.index, NVDA, label='NVDA')
plt.plot(TESLA.index, TESLA, label='Tesla')
plt.xlabel('Date')
plt.ylabel('Adj Close Price (USD)')
plt.title('NVDA and Tesla Stock Prices - YTD: {}% for NVDA, {}% for Tesla'.format(round(NVDA_YTD*100, 2), round(TESLA_YTD*100, 2)))
plt.legend()
plt.grid(which='major', linestyle='-.', linewidth='0.5', color='gray')
plt.show()