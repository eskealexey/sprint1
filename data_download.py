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
    try:
        average_price = total / len(data['Close'])
        return average_price
    except ZeroDivisionError:
        return 0


def notify_if_strong_fluctuations(data, threshold):
    lst = []
    midle = calculate_and_display_average_price(data)
    response_threshold = float(threshold) * midle / 100
    for i in data['Close']:
        lst.append(i)
    difference = max(lst) - min(lst)
    if difference > response_threshold:
        return f'Цена акций колебалась более чем на {threshold} процент за период'
    else:
        return ''
