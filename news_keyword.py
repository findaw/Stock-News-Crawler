import pandas as pd
from konlpy.tag import Okt
from collections import Counter
import os
# from korean import Noun
from datetime import timedelta
from datetime import datetime 
from crawllib.keyword import get_keywords, search_keyword


KEYWORD = ['NAVER', 'SK하이닉스', '삼성전자', '삼성전자우', '카카오']


def get_news_date_range(data, start_date, end_date, type = -1):
    type_word = '하락' if type==-1 else '상승'
    start_dt = datetime.strptime(start_date, '%Y.%m.%d')
    end_dt = datetime.strptime(end_date, '%Y.%m.%d')
    
    target_news = data[(news_list.date >= start_dt) & (news_list.date <= end_dt)]
    get_keywords(target_news, target, 50)
    search_keyword(target_news, 'MRO')
    pd.DataFrame(result.__next__(), columns=['키워드', '빈도수']).to_csv(f'data/keyword/삼성전자_{start_date}~{end_date}_{type_word}_키워드 빈도수.csv')

if __name__ == '__main__':
    target = '삼성전자'
    news_list = pd.read_csv(f'data/news/{target}_뉴스목록_10년.csv', dtype={'code':str}, index_col=[0])
    news_list.dropna(axis=0, inplace=True)
    news_list.date = pd.to_datetime(news_list.date, format='%Y.%m.%d')
    date_list = sorted(set(news_list.date))[198:200]
    days_step = 4

    for date in date_list:
        print(date)
        # 날짜 범위 지정
        min_date= date - timedelta(days=days_step)
        daily_news = news_list[(news_list.date >= min_date) & (news_list.date <= date)]
        print(daily_news.sort_values(by='date'))
        get_news_date_range(news_list, '2011.08.01', '2011.08.05')
        get_keywords(daily_news, target, 50)
        result = search_keyword(daily_news, 'MRO')
        
else:

    path_dir = os.getcwd() +'\data\\news'
    file_list = os.listdir(path_dir)

    for file_name in file_list:
        df_data = pd.read_csv(f'{path_dir}\\{file_name}')
        code_name = file_name.split('_')[0]
        get_keywords(df_data, code_name)

