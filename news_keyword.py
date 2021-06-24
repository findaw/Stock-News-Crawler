import pandas as pd
from konlpy.tag import Okt
from collections import Counter
import os
# from korean import Noun
from datetime import timedelta
from datetime import datetime 
from crawllib.keyword import get_keywords, search_keyword
from multiprocessing import Process

KEYWORD = ['NAVER', 'SK하이닉스', '삼성전자', '삼성전자우', '카카오']


def get_news_date_range(data, target, start_date, end_date, type = -1):
    type_word = '하락' if type==-1 else '상승'
    start_dt = datetime.strptime(start_date, '%Y.%m.%d')
    end_dt = datetime.strptime(end_date, '%Y.%m.%d')
    
    target_news = data[(data.date >= start_dt) & (data.date <= end_dt)]
    result = get_keywords(target_news, target, 200)
    pd.DataFrame(result.__next__(), columns=['키워드', '빈도수']).to_csv(f'data/keyword/{target}_{start_date}~{end_date}_{type_word}_키워드 빈도수.csv')
    
    # target_word = 'MRO'
    # result2 = search_keyword(target_news, target_word)
    # pd.DataFrame(result2.__next__(), columns=['키워드', '빈도수']).to_csv(f'data/keyword/삼성전자_{start_date}~{end_date}_{target_word} 관련_{type_word}_키워드 빈도수.csv')

if __name__ == '__main__':
    target = '삼성전자'
    news_list = pd.read_csv(f'data/news/{target}_뉴스목록_10년.csv', dtype={'code':str}, index_col=[0])
    news_list.dropna(axis=0, inplace=True)
    news_list.date = pd.to_datetime(news_list.date, format='%Y.%m.%d')
    date_list = sorted(set(news_list.date))[198:200]
    days_step = 4

    procs = []
    
    # """하락 키워드 추출"""
    start_list = ['2011.08.01', '2012.05.09', '2013.06.07', '2014.06.13', '2015.04.17',
    '2016.01.22', '2017.07.28', '2017.11.17','2018.01.01','2019.04.12','2020.02.21']
    end_list = ['2011.08.19', '2012.09.08', '2013.07.05','2014.10.17','2015.08.28',
    '2016.03.25', '2017.08.11','2018.02.09','2018.02.09','2019.05.17','2020.03.20']
    for start, end in zip(start_list, end_list):
        proc = Process(target =get_news_date_range, args=(news_list, target, start, end, -1))
        procs.append(proc)
        proc.start()

    # # """상승 키워드 추출"""
    # start_list = ['2011.08.26', '' ]
    # end_list = ['2011.08.19', ]
    # for start, end in zip(start_list, end_list):
    #     proc = Process(target =get_news_date_range, args=(news_list, start, end, 1))
    #     procs.append(proc)
    #     proc.start()

    for proc in procs:
        proc.join()


    # for date in date_list:
    #     print(date)
    #     # 날짜 범위 지정
    #     min_date= date - timedelta(days=days_step)
    #     daily_news = news_list[(news_list.date >= min_date) & (news_list.date <= date)]
    #     print(daily_news.sort_values(by='date'))
    #     get_news_date_range(news_list, '2011.08.01', '2011.08.05')
    #     get_keywords(daily_news, target, 50)
    #     result = search_keyword(daily_news, 'MRO')
        
else:

    path_dir = os.getcwd() +'\data\\news'
    file_list = os.listdir(path_dir)

    for file_name in file_list:
        df_data = pd.read_csv(f'{path_dir}\\{file_name}')
        code_name = file_name.split('_')[0]
        get_keywords(df_data, code_name)

