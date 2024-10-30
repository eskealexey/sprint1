import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import plotly
import plotly.graph_objs as go
import plotly.express as px
from plotly.graph_objs import Figure
from plotly.subplots import make_subplots

def create_and_save_plot(data, ticker, mdac, period=None, start_date=None, end_date=None, style=None, filename=None):
    plt.figure(figsize=(15, 9))

    if style == '1':
        pass
    elif style == '2':
        plt.style.use('ggplot')
    elif style == '3':
        plt.style.use('fivethirtyeight')
    elif style == '4':
        plt.style.use('dark_background')
    elif style == '5':
        plt.style.use('grayscale')

    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            plt.subplots_adjust(left=0.13,
                                right=0.93,
                                top=0.9,
                                bottom=0.15,
                                wspace=0.1,
                                hspace=0.5)
            plt.subplot(2, 1, 1)
            plt.title(f"{ticker} Цена акций с течением времени")
            plt.xlabel("Дата")
            plt.ylabel("Цена")
            dates = data.index.to_numpy()
            plt.plot(dates, data['Close'].values, label='Close Price')
            plt.plot(dates, data['Moving_Average'].values, label='Moving Average')
            plt.legend()
            plt.xticks(rotation=45)
            plt.subplot(2, 1, 2)
            plt.title(f"{ticker} индикатор MACD")
            plt.xlabel("Дата")
            plt.plot(dates, mdac[0].values, label='Signal')
            plt.plot(dates, mdac[1].values, label='MACD')
            plt.legend()
            plt.xticks(rotation=45)

        else:
            print("Информация о дате отсутствует или не имеет распознаваемого формата.")
            return
    else:
        if not pd.api.types.is_datetime64_any_dtype(data['Date']):
            data['Date'] = pd.to_datetime(data['Date'])
        plt.subplots_adjust(left=0.13,
                            right=0.93,
                            top=0.9,
                            bottom=0.15,
                            wspace=0.1,
                            hspace=0.5)
        plt.subplot(2, 1, 1)
        plt.title(f"{ticker} Цена акций с течением времени")
        plt.xlabel("Дата")
        plt.ylabel("Цена")
        plt.plot(data['Date'], data['Close'], label='Close Price')
        plt.plot(data['Date'], data['Moving_Average'], label='Moving Average')
        plt.legend()
        plt.xticks(rotation=45)
        plt.subplot(2, 1, 2)
        plt.title(f"{ticker} индикатор MACD")
        plt.xlabel("Дата")
        plt.plot(data['Date'], mdac[0].values, label='Signal')
        plt.plot(data['Date'], mdac[1].values, label='MACD')
        plt.legend()
        plt.xticks(rotation=45)


    if filename is None:
        if period is None:
            filename = f"{ticker}_{start_date}_{end_date}_stock_price_chart.png"
        else:
            filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")


def show_data(data, ticker, macd):
    '''
    Функция для отображения данных в виде графика используя библиотеку plotly
    '''
    if 'Date' not in data:
        if pd.api.types.is_datetime64_any_dtype(data.index):
            dates = data.index.to_numpy()
            # fig = go.Figure()
            fig = make_subplots(rows=2, cols=1)

            fig.add_trace(go.Scatter(x=dates, y=data['Close'],
                                     mode='lines+markers',
                                     name='Close Price'),
                                     row=1, col=1)
            fig.add_trace(go.Scatter(x=dates, y=data['Moving_Average'],
                                     mode='lines+markers',
                                     name='Moving_Average'),
                                     row=1, col=1)
            fig.update_layout(legend_orientation="h",
                              legend=dict(x=.5, xanchor="center"),
                              title=ticker.upper(),
                              xaxis_title="Date",
                              yaxis_title="Price",
                              margin=dict(l=0, r=0, t=30, b=0))

            fig.add_trace(go.Scatter(x=dates, y=macd[0].values,
                                     mode='lines',
                                     name='Signal'),
                          row=2, col=1)
            fig.add_trace(go.Scatter(x=dates, y=macd[1].values,
                                     mode='lines',
                                     name='MACD'),
                          row=2, col=1)
            fig.update_layout(legend_orientation="h",
                              legend=dict(x=.5, xanchor="center"),
                              title=ticker.upper(),
                              xaxis_title="Date",
                              yaxis_title="Price",
                              margin=dict(l=0, r=0, t=30, b=0))
            fig.show()
