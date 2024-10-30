import data_download as dd
import data_plotting as dplt


def main():
    period, start_date, end_date = None, None, None
    print("Добро пожаловать в инструмент получения и построения графиков биржевых данных.")
    print("Вот несколько примеров биржевых тикеров, которые вы можете рассмотреть: AAPL (Apple Inc), GOOGL (Alphabet Inc), MSFT (Microsoft Corporation), AMZN (Amazon.com Inc), TSLA (Tesla Inc).")
    print("Общие периоды времени для данных о запасах включают: 1д, 5д, 1мес, 3мес, 6мес, 1г, 2г, 5г, 10л, с начала года, макс.")
    ticker = input("Введите тикер акции (например, «AAPL» для Apple Inc):»")

    while True:
        flag = input("Введите 1, если вы хотите получить график за период, и 0, если хотите получить график за произвольный интервал: ")
        if flag== '1':
            period = input("Введите период для данных (например, '1mo' для одного месяца): ")
            break
        elif flag== '0':
            start_date = input("Введите дату начала периода (например, '2024-10-10'): ")
            end_date = input("Введите дату конца периода (например, '2024-10-20'): ")
            break
        else:
            continue

    threshold = input(f"Укажите порог срабатывания флуктуаций в % (например, 0.05): ")
    filename = input("Введите имя файла для сохранения данных (например, 'stock_data.csv'): ")

    print('Необходимо выбрать стиль оформления графиков.')
    print('Выберите один из следующих стилей:')
    print('1. Стандартный')
    print('2. "ggplot"')
    print('3. "fivethirtyeight"')
    print('4. "dark_background"')
    print('5. "grayscale"')
    while True:
        style = input("Введите стиль графика (1, 2, 3, 4, 5): ")
        if style not in ['1','2','3','4','5']:
            continue
        else:
            break

    # Fetch stock data
    stock_data = dd.fetch_stock_data(ticker,period=period, start_date=start_date, end_date=end_date)

    # Add moving average to the data
    stock_data = dd.add_moving_average(stock_data)

    # Calculate and display the average price
    print(f'Средняя цена закрытия акций за заданный период - {dd.calculate_and_display_average_price(stock_data)}')

    # Notify if there are any strong fluctuations
    print(dd.notify_if_strong_fluctuations(stock_data, threshold=threshold))

    # Upload stock data to a CSV file
    dd.export_data_to_csv(stock_data, filename)

    # Adding additional technical indicators MACD
    macd = dd.calc_indicators_MACD(stock_data)

    # Calculating standard deviation of closing price
    sd = dd.calculate_standard_deviation(stock_data)
    print('Стандартное отклонение = {}'.format(sd))

    # Plot the data
    dplt.create_and_save_plot(stock_data, ticker, macd, period, start_date, end_date, style=style)

    # Function for displaying data as a graph using the plotly library
    dplt.show_data(stock_data, ticker, macd)

if __name__ == "__main__":
    main()
