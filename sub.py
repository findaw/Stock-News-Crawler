from crawllib.crawler import Crawler
from bs4 import BeautifulSoup
from selenium import webdriver as WebDriver
import pandas as pd

search_word = "현대차"
start_date = "2020.12.20"
end_date = "2021.06.03"
sort_type = Crawler.Sort_Best
max_page = 4000   # 4000

# Daum News search Url
# https://search.daum.net/search?w=news&DA=STC&enc=utf8&cluster=y&cluster_page=1&q={search_word}&p={page_no}&sd={start_date}000000&ed={end_date}235959&period=u



"""
: 네이버 뉴스는 결과물을 최대 4000개까지만 반환한다 
: 따라서 한번에 date를 길게 넣으면 모든 결과를 못얻는다 
: 모든 결과를 수집하기 위한 추가 로직이 필요하다 !
: 1) date 단위를 나누면서 request
: 2) paging시 마지막 page_no 에서 반복문 나가기
"""

result = []
for page_no in range(1,max_page,10):
    url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sort={str(sort_type)}&pd=3&ds={start_date}&de={end_date}&start={page_no}'
    print(url)
    crawler = Crawler()
    res = crawler.get_url_data(url)
    soupData = BeautifulSoup(res.content, 'html.parser')

    news_list = soupData.select('.news_tit')
    desc = soupData.select('.api_txt_lines.dsc_txt_wrap')
    for title_addr, content in zip(news_list, desc):
        print(title_addr['href'])
        print(title_addr['title'])
        print(content.text)
        result.append([title_addr['title'] ,title_addr['href'] , content.text])

df_news = pd.DataFrame(result, columns=['title', 'link', 'content'])
df_news.to_csv('data/%s_네이버_뉴스목록_%s~%s.csv'%(search_word, start_date, end_date))



# for link in df_news.link[:2]:
#     print(link)
#     res = crawler.get_url_data(link)
#     soupData = BeautifulSoup(res.content, 'html.parser')
#     for item in soupData.div:
#         print(item)
#     print('*'*50)


# js -> document.defaultView.getComputedStyle(document.querySelectorAll('div')[40])['fontSize']