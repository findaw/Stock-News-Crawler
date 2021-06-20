from crawllib.crawler import NewsCrawler
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta as td
from multiprocessing import Process


top_no=5
kospi_top = pd.read_csv('data/sise_market_sum.csv', index_col=[0])[:top_no]

def worker(data, start_index, start, end):
    start_date = dt.strptime(start, '%Y%M%d')  
    end_date = dt.strptime(end, '%Y%M%d')
    for index in range(start_index,start_index+1):
        try:
            search_word, code = data.title[index], data.code[index]
        except Exception as e:
            print('[Error] : ', e)
            continue
        
        result = []
        while start_date.strftime('%Y%m%d') != end_date.strftime('%Y%m%d'):
            vdate = start_date.strftime('%Y%m%d')
            date = '%s.%s.%s' % (vdate[0:4],vdate[4:6],vdate[6:])
            print(date)
            result += NewsCrawler().scrapy_naver(code, search_word, date, date, NewsCrawler.SORT_BEST)
            start_date += td(days=1)
        # end : for in date:
        try:
            df_news = pd.DataFrame(result[1:], columns=['code', 'date', 'title', 'link', 'content'])
            df_news.to_csv('data/news/%s_네이버_뉴스목록_1년_%s~%s.csv'%(search_word, start, end))
        except:
            pass
    # end : for in code:


if __name__ == '__main__':
    procs = []
    for n in range(1, 2):
        index = n
        data = kospi_top[index:index+1]
        start_date = [date for date in range(20100101,20210620,10000)]
        end_date = [date for date in range(20110101,20220620,10000)]
        for start, end in zip(start_date, end_date):
            worker(data, index, str(start),str(end))
            # proc = Process(target =worker, args=(data, index, start, end))
            # procs.append(proc)
            # proc.start()

    # for proc in procs:
    #     proc.join()
