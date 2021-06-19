## 클리앙 주식한당 스크래핑


import time
from bs4 import BeautifulSoup
from crawllib.crawler import Crawler
import pandas as pd
from requests.exceptions import SSLError

origin_url = 'https://www.clien.net'
result = []

for page in range(1370):
    #for page in range():
    print(page)
    crawler = Crawler()
    res = crawler.get_url_data(f"https://www.clien.net/service/board/cm_stock?&od=T31&category=0&po={page}")
    soupData = BeautifulSoup(res.content, 'html.parser') 

    for a_tag in soupData.select('.list_subject'):
        res = crawler.get_url_data(origin_url + a_tag['href']) 
        soupData = BeautifulSoup(res.content, 'html.parser') 
        try:
            title_node = soupData.select('.post_subject span')
            category = title_node[0].text.strip()                   # 게시글 카테고리
            title = title_node[1].text.strip()                      # 제목
            datetime = soupData.select('.fa.fa-clock-o')[0].nextSibling.strip()     # datetime
            content = soupData.select('.post_article')[0].text.strip()
            result.append([category, datetime, title, content])
        except Exception or SSLError as e:
            print('[Error]', e)
            continue
        except:
            print('[Error]', e)
            continue
        finally:
            time.sleep(6000)

    

df = pd.DataFrame(result, columns=['category', 'datetime', 'title', 'content'])
df.to_csv('data/clien_stock_board.xlsx', sep='@')





