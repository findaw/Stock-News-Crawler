# pip install mplfinance
# pip install mpl_finance

from re import S
from mpl_finance import candlestick2_ohlc
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd
from pandas_datareader import data  
from datetime import datetime
from IPython.display import display



sise_day_list = pd.read_csv('data/sise_day_digit.csv', index_col=0)


for code in set(sise_day_list.code):
    mark = sise_day_list.code==code
    stock_item = sise_day_list[mark]

    stock_item['MA3'] = stock_item['close'].rolling(3).mean()
    stock_item['MA5'] = stock_item['close'].rolling(5).mean()
    stock_item['MA10'] = stock_item['close'].rolling(10).mean()
    stock_item['MA20'] = stock_item['close'].rolling(20).mean()

    fig, ax = plt.subplots(figsize=(20,10))
    
    target_name =list(stock_item['한글 종목약명'])[0] 
    ax.set_title(f'{target_name} 주가 그래프', fontsize=15)
    ax.set_ylabel('주가')
    ax.set_xlabel('날짜')
    ax.plot(stock_item.index, stock_item[['close', 'MA5', 'MA10']])
    ax.legend(['Close', 'MA5', 'MA10'])
    plt.show()
    
    ax = fig.add_subplot(111)
    index = stock_item

    # 그래프 그리기
    fig = plt.subplots(figsize=(20,10))
    ax = fig.add_subplot(111)
    index = stock_item['date']

    ax.plot(index, stock_item['MA3'], label='MA3', linewidth=0.7)
    ax.plot(index, stock_item['MA5'], label='MA5', linewidth=0.7)
    ax.plot(index, stock_item['MA10'], label='MA10', linewidth=0.7)

    ax.xaxis.set_major_locator(ticker.MaxNLocator(20))      # x축 티커 20 개로 제한

    ax.set_title('KOSPI INDEX', fontsize=22)
    ax.set_ylabel("주가")
    ax.set_xlabel("날짜")
    
    candlestick2_ohlc(ax, stock_item['open'], stock_item['high'], stock_item['low'], stock_item['close'], width=0.5, colorup='r', colordown='b')

    ax.legend()
    ax.grid()
    plt.show()