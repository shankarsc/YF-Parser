import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import datetime as dt

import warnings
warnings.filterwarnings("ignore")

def get(ticker, startdate, enddate):
    """
    Return asset data (Date, OHLC) from Yahoo Finance
    """
    def data(ticker):
        return (pdr.get_data_yahoo(ticker, startdate, enddate))
    
    datas = map(data, ticker)
    return (pd.concat(datas, keys=ticker, names=['Ticker', 'Date']))

def set_daily_close_change(ticker, startdate, enddate):
    """
    Compiles returned data based on 'Adj Close' column for all assets
    Removes NaN by fill-forward method
    """
    # Isolate the 'Adj Close' values and pivot the DataFrame
    all_data = get(ticker, startdate, enddate)
    daily_close_px = all_data[['Adj Close']].reset_index().pivot_table(index=['Date'], columns=['Ticker'], values=['Adj Close'])

    # Obtain the daily percentage change in price of assets
    daily_close_change = pd.DataFrame(index=daily_close_px.index, columns=daily_close_px.columns)
    daily_close_change = daily_close_px['Adj Close'].shift(-1) - daily_close_px['Adj Close']
    
    # Eliminate the NaN values using forward-fill values
    daily_close_change = daily_close_change.fillna(method='ffill')
    daily_close_change = daily_close_change.dropna()
    
    return daily_close_change