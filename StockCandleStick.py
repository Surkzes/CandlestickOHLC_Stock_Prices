import pandas as pd
import numpy as np
from pandas_datareader import data as wb
import matplotlib.pyplot as plt
from mplfinance import *
import matplotlib.dates as mpl_dates
import plotly.graph_objects as go
import io

#   Pull Data
def get_candlestick_data(ticker, startdate, enddate):  
    
    # Pull Stock Data
    stock_data = pd.DataFrame()
    stock_data = wb.DataReader(ticker, data_source="yahoo", start=startdate, end=enddate)
    
    candlestick = go.Candlestick(
                            x=stock_data.index,
                            open=stock_data['Open'],
                            high=stock_data['High'],
                            low=stock_data['Low'],
                            close=stock_data['Close']
                            )
    save_fig(candlestick, ticker)
    
    #plot_fig(candlestick, ticker)
    

def save_fig(data, ticker):
    fig = go.Figure(data=[data])
    
    fig.update_layout(
        title='Open High Low Close Candle Stick Graphs',
        yaxis_title= ticker + ' Price $',
        xaxis_rangeslider_visible=False)
    
    fig.write_image("temp.png")
    
def plot_fig(data, ticker):
    fig = go.Figure(data=[data])
    
    fig.update_layout(
        title='Open High Low Close Candle Stick Graphs',
        yaxis_title= ticker + ' Price $')
    fig.show()


get_candlestick_data('SPY', '2020-01-01', '2020-04-01')