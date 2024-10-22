import matplotlib.pyplot as plt
import pandas as pd


def create_and_save_plot(data, ticker, period, mdac, filename=None):
    plt.figure(figsize=(15, 9))

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
        filename = f"{ticker}_{period}_stock_price_chart.png"

    plt.savefig(filename)
    print(f"График сохранен как {filename}")
