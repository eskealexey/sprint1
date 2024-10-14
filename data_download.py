from functools import total_ordering

import yfinance as yf


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    total = 0
    for i in data['Close']:
        total += i
    average_price = total / len(data['Close'])
    return f'Средняя цена закрытия акций за заданный период - {average_price}'
