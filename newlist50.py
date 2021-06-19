from crawllib.crawler import NewsCrawler
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
from multiprocessing import Process


top_no=50
kospi_top = pd.read_csv('data/sise_market_sum.csv', index_col=[0])[:top_no]

def worker(data, start_index):
    start_date = dt.strptime('20110619', '%Y%M%d')  
    end_date = dt.strptime('20210619', '%Y%M%d')
    for index in range(start_index,start_index+10):
        try:
            search_word, code = data.title[index], data.code[index]
            search_word = data.title[index]
            type(search_word)
            print(search_word)
        except Exception as e:
            print('[Error] : ', e)
            continue
        
        result = []
        while start_date.strftime('%Y%m%d') != end_date.strftime('%Y%m%d'):
            vdate = start_date.strftime('%Y%m%d')
            date = '%s.%s.%s' % (vdate[0:4],vdate[4:6],vdate[6:])
            result += NewsCrawler().scrapy_naver(code, search_word, date, date, NewsCrawler.SORT_BEST)
            start_date += td(days=1)
        # end : for in date:
        print(result)
        df_news = pd.DataFrame(result[1:], columns=['code', 'date', 'title', 'link', 'content'])
        df_news.to_csv('data/news/%s_네이버_뉴스목록_10년.csv'%(search_word))
    # end : for in code:


if __name__ == '__main__':
    procs = []
    for n in range(5):
        index = 10*n
        data = kospi_top[index:index+10]
        proc = Process(target =worker, args=(data, index))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
