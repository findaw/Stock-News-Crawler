import requests 
from typing import Final
from requests.models import Response
from bs4 import BeautifulSoup
import time

class Crawler():
    def __init__(self, url=''):
        self.url = url

    def get_url_data(self, url='') -> Response:
        time.sleep(0.01)
        if (url == '' ) and (self.url != ''):
            url = self.url
        headers = {'User-Agent' : 'Mozilla/5.0',}
        try:
            return requests.get(url, headers=headers)
        except requests.exceptions as re:
            print('[Error] : get_url_data')
            print(re)
            return False
    
class NewsCrawler(Crawler):
    SORT_BEST : Final = 0
    SORT_LATEST : Final = 1
    SORT_OLDEST : Final = 2
    MAX_PAGE : Final  = 4000

    def __init__(self, search_word=''):
        self.search_word = search_word
        
    def scrapy_naver(self, code , search_word : str, start_date: str, end_date:str, sort_type=0 ) -> list: 
        result = [""]
        if search_word == '' and self.search_word != '' :
            search_word = self.search_word
        
        last_line = ""
        for page_no in range(1, self.MAX_PAGE, 10):
                url = f'https://search.naver.com/search.naver?where=news&query={search_word}&sort={str(sort_type)}&pd=3&ds={start_date}&de={end_date}&start={page_no}'
                print(url)
                res = self.get_url_data(url)
                soupData = BeautifulSoup(res.content, 'html.parser')
                news_list = soupData.select('.news_tit')
                desc = soupData.select('.api_txt_lines.dsc_txt_wrap')
                news_row = ""
                if desc == []:
                    return result
                for title_addr, content in zip(news_list, desc):
                    news_row = [code, start_date, title_addr['title'] ,title_addr['href'] , content.text]
                    if(last_line != news_row):      # is not  : id  / != : value
                        result.append(news_row)
                        last_line = news_row
                    else:
                        return result
    