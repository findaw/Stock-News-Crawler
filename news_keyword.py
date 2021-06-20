import pandas as pd
from konlpy.tag import Okt
from collections import Counter
import os
# from korean import Noun
from datetime import timedelta
from datetime import datetime 

def get_keywords(data, keyword):

    daily_phrases = []
    daily_morphs = []
    daily_nouns = []
    text_list = data['content']   #Series
    okt = Okt()

    stopwords = []
    with open('res/stopwords.txt', 'rt', encoding='UTF8') as f:
        stopwords = f.read().splitlines()

    def filter_keyword(text, func, stopwords):
        word_list = func(text)
        stopwords += [keyword]
        return [i for i in word_list if i not in stopwords and len(i) > 1]

    for i in range(len(data)):
        text = text_list[i]
        daily_phrases += filter_keyword(text, okt.phrases, stopwords)
        daily_morphs += filter_keyword(text, okt.morphs, stopwords)    
        daily_nouns += filter_keyword(text, okt.nouns, stopwords)
    
    def get_top_50(wlist):
        # TOP 50 글자
        counter = Counter(wlist)
        total_sentence_50 = counter.most_common(50)
        print(total_sentence_50)
        return total_sentence_50
    
    get_top_50(daily_phrases)
    get_top_50(daily_morphs)
    get_top_50(daily_nouns)


KEYWORD = ['NAVER', 'SK하이닉스', '삼성전자', '삼성전자우', '카카오']


if __name__ == '__main__':
    news_list = pd.read_csv('data/news/카카오_뉴스목록_10년.csv', dtype={'code':str}, index_col=[0])
    news_list.dropna(axis=0, inplace=True)
    news_list.date = pd.to_datetime(news_list.date, format='%Y.%m.%d')
    days_step = 5
    date_list = sorted(set(news_list.date))[:10]


    for date in date_list:
        print(date)
        # 날짜 범위 지정
        min_date= date - timedelta(days=days_step)
        daily_news = news_list[(news_list.date >= min_date) & (news_list.date <= date)]
        print(daily_news.sort_values(by='date'))
        get_keywords(daily_news, '카카오')
else:

    path_dir = os.getcwd() +'\data\\news'
    file_list = os.listdir(path_dir)

    for file_name in file_list:
        df_data = pd.read_csv(f'{path_dir}\\{file_name}')
        code_name = file_name.split('_')[0]
        get_keywords(df_data, code_name)

