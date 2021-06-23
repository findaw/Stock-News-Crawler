from crawllib.crawler import NewsCrawler
import pandas as pd

rate_best_data = pd.read_csv('data/급등주포착_최종.csv', index_col=[0])
count = 0
for code in set(rate_best_data.code):
    mask = rate_best_data.code==code
    rate_best_data[mask]
    try:
        search_word = rate_best_data[mask]
        search_word = search_word['한글 종목약명']    # Series
        search_word = list(search_word.values)[0].replace('보통주','').strip()  # index 매치가 안되어서 list로 형변환
    except Exception as e:
        print('krx_code와 매치되지않음(종목명X) : ', code)
        continue
    date_list = list(rate_best_data[mask]['date'].values)
    start_date = date_list[0]
    end_date = date_list[-1]
    result = []
    for date in date_list:
        result += NewsCrawler().scrapy_naver(code, search_word, date, date, NewsCrawler.SORT_BEST)
        
    # end : for in date:
    print(result)
    df_news = pd.DataFrame(result[1:], columns=['code', 'date', 'title', 'link', 'content'])
    df_news.to_csv('data/news/%s_네이버_뉴스목록_%s-%s.csv'%(search_word, start_date, end_date))
# end : for in code:
           