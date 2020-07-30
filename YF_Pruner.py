import pandas as pd
import pandas_datareader as pdr
import yfinance as yf
import datetime as dt

import warnings
warnings.filterwarnings("ignore")

def get_all(ticker, startdate, enddate):
    """
    Return asset data (Date, OHLC) from Yahoo Finance
    """
    def data(ticker):
        return (pdr.get_data_yahoo(ticker, startdate, enddate))
    
    datas = map(data, ticker)
    return (pd.concat(datas, keys=ticker, names=['Ticker', 'Date']))

def get_daily_open(ticker, startdate, enddate):
    """
    Returns data for 'Open' column for all assets
    """
    # Isolate the 'Open' values and pivot the DataFrame
    all_data = get_all(ticker, startdate, enddate)
    daily_open = all_data[['Open']].reset_index().pivot_table(index=['Date'], columns=['Ticker'], values=['Open'])
    
    return daily_open

def get_daily_high(ticker, startdate, enddate):
    """
    Returns data for 'High' column for all assets
    """
    # Isolate the 'High' values and pivot the DataFrame
    all_data = get_all(ticker, startdate, enddate)
    daily_high = all_data[['High']].reset_index().pivot_table(index=['Date'], columns=['Ticker'], values=['High'])
    
    return daily_high

def get_daily_low(ticker, startdate, enddate):
    """
    Returns data for 'Low' column for all assets
    """
    # Isolate the 'Low' values and pivot the DataFrame
    all_data = get_all(ticker, startdate, enddate)
    daily_low = all_data[['Open']].reset_index().pivot_table(index=['Date'], columns=['Ticker'], values=['Open'])
    
    return daily_low

def get_daily_close(ticker, startdate, enddate):
    """
    Returns data for 'Close' column for all assets
    """
    # Isolate the 'Close' values and pivot the DataFrame
    all_data = get_all(ticker, startdate, enddate)
    daily_close = all_data[['Close']].reset_index().pivot_table(index=['Date'], columns=['Ticker'], values=['Close'])
    
    return daily_close


def get_daily_adj_close(ticker, startdate, enddate):
    """
    Returns data for 'Adj Close' column for all assets
    """
    # Isolate the 'Adj Close' values and pivot the DataFrame
    all_data = get_all(ticker, startdate, enddate)
    daily_adj_close = all_data[['Adj Close']].reset_index().pivot_table(index=['Date'], columns=['Ticker'], values=['Adj Close'])
    
    return daily_adj_close

def get_daily_volume(ticker, startdate, enddate):
    """
    Returns data for 'Volume' column for all assets
    """
    # Isolate the 'Adj Close' values and pivot the DataFrame
    all_data = get_all(ticker, startdate, enddate)
    daily_volume = all_data[['Volume']].reset_index().pivot_table(index=['Date'], columns=['Ticker'], values=['Volume'])
    
    return daily_volume

def get_daily_change(data):
    """
    Returns the daily change for the selected column
    """
    return (data.shift(-1) - data).fillna(method='ffill').dropna()

def get_prct_change(data):
    """
    Obtain the daily percentage change for the price data 
    """
    return ((data.shift(-1)-data)/data).fillna(method='ffill').dropna()