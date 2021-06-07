from crawllib.crawler import Crawler
from bs4 import BeautifulSoup
import pandas as pd

rate_best_data = pd.read_csv('data/급등주포착_최종.csv', index_col=[0])

for code in set(rate_best_data.code):
    mark = rate_best_data.code==code
    rate_best_data[mark]
    try:

        code_sise_data = rate_best_data[mark].values
        search_word = rate_best_data[mark]
        search_word = search_word['한글 종목약명']    # Series
        search_word = list(search_word.values)[0].replace('보통주','').strip()  # index 매치가 안되어서 list로 형변환
    except Exception as e:
        print('krx_code와 매치되지않음(종목명X) : ', code)
        continue
    date_list = list(rate_best_data[mark]['date'].values)
    start_date = date_list[0]
    end_date = date_list[-1]
    result = [""]
    for date in date_list:
        sort_type = Crawler.Sort_Best
        max_page = 4000   # 4000
        last_line = ""
        for page_no in range(1,max_page,10):
            url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sort={str(sort_type)}&pd=3&ds={date}&de={date}&start={page_no}'
            print(url)
            crawler = Crawler()
            res = crawler.get_url_data(url)
            soupData = BeautifulSoup(res.content, 'html.parser')

            news_list = soupData.select('.news_tit')
            desc = soupData.select('.api_txt_lines.dsc_txt_wrap')
            news_row = ""
            for title_addr, content in zip(news_list, desc):
                print(title_addr['href'])
                print(title_addr['title'])
                #print(content.text)
                
                news_row = [code, date, title_addr['title'] ,title_addr['href'] , content.text]
            
            # 마지막 페이지인지 검사
            print(last_line != news_row)
            if(last_line != news_row):      # is not  : id  / != : value
                result.append(news_row)
                last_line = news_row
            else:
                break

        # end : for range(1,max_page,10):
    # end : for list(rate_best_data[mark]['date'].values):
    print(result)
    df_news = pd.DataFrame(result[1:], columns=['code', 'date', 'title', 'link', 'content'])
    df_news.to_csv('data/news/%s_네이버_뉴스목록_%s-%s.csv'%(search_word, start_date, end_date))
# end : for set(rate_best_data.code):
           