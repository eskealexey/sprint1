import yfinance as yf
from pandas import DataFrame


def fetch_stock_data(ticker, period='1mo'):
    stock = yf.Ticker(ticker)
    data = stock.history(period=period)
    return data


def add_moving_average(data, window_size=5):
    data['Moving_Average'] = data['Close'].rolling(window=window_size).mean()
    return data


def calculate_and_display_average_price(data):
    '''
    Функция вычисляет и выводит среднюю цену за период
    '''

    total = 0
    for i in data['Close']:
        total += i
    try:
        average_price = total / len(data['Close'])
        return average_price
    except ZeroDivisionError:
        return 0


def notify_if_strong_fluctuations(data, threshold):
    '''
    Функция проверяет наличие сильных колебаний цены акций,
    в случае превышения заданного порога вывводит сообщение
    '''
    lst = []
    if threshold == '':
        return ''
    else:
        midle = calculate_and_display_average_price(data)
        response_threshold = float(threshold) * midle / 100
        for i in data['Close']:
            lst.append(i)
        difference = max(lst) - min(lst)
        if difference > response_threshold:
            return f'Цена акций колебалась более чем на {threshold} процент за период'
        else:
            return ''


def create_filename(filename):
    '''
    Функция формирует имя файла для экспорта данных
    '''
    if filename == '':
        return 'data.csv'
    else:
        if len(filename) < 4 or filename[-4:] != '.csv':
            filename += '.csv'
        else:
            filename = filename
    return filename


def export_data_to_csv(data, filename):
    '''
    Функция экспортирует данные в csv файл
    '''
    name_csv = create_filename(filename)
    data.to_csv(name_csv)


def calc_indicators_MACD(data: DataFrame):
    '''
    Функция добавления индикатора MACD
    '''
    ema12 = data['Close'].ewm(span=12, adjust=False).mean()
    ema26 = data['Close'].ewm(span=26, adjust=False).mean()
    macd = ema12 - ema26
    signal = macd.ewm(span=9, adjust=False).mean()
    gist = macd - signal

    return signal, macd, gist


