# -*- coding: utf-8 -*-
"""prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/18qJw_0S7uqq4tgmomj55HNo9Pu45-D2D
"""

import time
  
  
while(True):
    import numpy as np
    import pandas as pd

    # Data Source
    import yfinance as yf

    # Data viz
    import plotly.offline
    import plotly.graph_objs as go

    data = yf.download(tickers='^NSEI', period='1d', interval='1m')
    # Interval required 1 minute
    data['Middle Band'] = data['Close'].rolling(window=21).mean()
    data['Upper Band'] = data['Middle Band'] + \
        1.96*data['Close'].rolling(window=21).std()
    data['Lower Band'] = data['Middle Band'] - \
        1.96*data['Close'].rolling(window=21).std()

    # declare figure
    fig = go.Figure()

    fig.add_trace(go.Scatter(x=data.index, y=data['Middle Band'], line=dict(
        color='blue', width=.7), name='Middle Band'))
    fig.add_trace(go.Scatter(x=data.index, y=data['Upper Band'], line=dict(
        color='red', width=1.5), name='Upper Band (Sell)'))
    fig.add_trace(go.Scatter(x=data.index, y=data['Lower Band'], line=dict(
        color='green', width=1.5), name='Lower Band (Buy)'))


    # Candlestick
    fig.add_trace(go.Candlestick(x=data.index,
                                open=data['Open'],
                                high=data['High'],
                                low=data['Low'],
                                close=data['Close'], name='market data'))

    # Add titles
    fig.update_layout(
        title='NSEI live price buy_sell prediction',
        yaxis_title='NIFTY50')

    # X-Axes
    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=15, label="15m", step="minute", stepmode="backward"),
                dict(count=45, label="45m", step="minute", stepmode="backward"),
                dict(count=1, label="HTD", step="hour", stepmode="todate"),
                dict(count=3, label="3h", step="hour", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    # Show
    fig.show()
    plotly.offline.plot(fig, filename=r'C:\Users\sidhu\Desktop\Final Project\Sem-6-Project\templates\positives.html')

    time.sleep(300)
