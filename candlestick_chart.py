# pip install mplfinance
# pip install mpl_finance
# pip install --upgrade mplfinance
# pip install pandas_datareader

from re import S
from mpl_finance import candlestick2_ohlc
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import pandas as pd
# from pandas_datareader import data  
from datetime import datetime
from IPython.display import display
from matplotlib import font_manager, rc


sise_day_list = pd.read_csv('data/sise_day_digit_name.csv', index_col=0)
sise_day_list['date'] = pd.to_datetime(sise_day_list['date'])
sise_day_list = sise_day_list.set_index(sise_day_list['date'])
sise_day_list.head()
sise_day_list = sise_day_list.iloc[::-1]

for code in set(sise_day_list.code):
    mark = sise_day_list.code==code
    stock_item = sise_day_list[mark]
    stock_item = stock_item[stock_item['volume'] > 0]       # 거래 휴일 필터
    
    # 그래프 그리기
    fig = plt.figure(figsize=(12,7))
    
    # 폰트 설정
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name() 
    rc('font', family=font_name)
    
    ax = fig.add_subplot(111)

    index = stock_item.index.astype('str')
    print(stock_item['close'].rolling(window=3).mean())
    ax.plot(index, stock_item['close'].rolling(window=3).mean(), label='MA3', linewidth=0.7)
    ax.plot(index, stock_item['close'].rolling(window=5).mean(), label='MA5', linewidth=0.7)
    ax.plot(index, stock_item['close'].rolling(window=10).mean(), label='MA10', linewidth=0.7)
    candlestick2_ohlc(ax, stock_item['open'], stock_item['high'], stock_item['low'], stock_item['close'], width=0.5, colorup='r', colordown='b')
      
    try:
        target_name =list(stock_item['한글 종목약명'])[0] 
        if target_name == None:
            continue
        ax.set_title(f'{target_name} 주가 그래프', fontsize=15)
    except Exception as e:
        print('krx_code와 매치되지않음(종목명X) : ', code)
        continue

    print(stock_item.head())
        
    plt.xticks(rotation=45)
    ax.set_ylabel("주가")
    ax.set_xlabel("날짜")
    ax.xaxis.set_major_locator(ticker.MaxNLocator(20))      # x축 티커 20 개로 제한

    ax.legend()
    ax.grid()
    plt.show()