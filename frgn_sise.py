from bs4 import BeautifulSoup
import pandas as pd 
import requests
from itertools import count
import time
result=[]
item_code = pd.read_csv('data/sise_code_Top50.csv', dtype={'code':str})['code'][:10]
print(item_code)
for code in item_code:
    stop_loop = False    # stop_loop 정의
    last_page_date = ""
    for page in count(1):
        url = f'https://finance.naver.com/item/frgn.nhn?code={code}&page={page}'
        html = requests.get(url, headers = {'User-Agent':'Mozilla/5.0'})
        soup_data = BeautifulSoup(html.content,'html.parser') 
        table = soup_data.findAll('table',{'class':'type2'})[1]  # table 원하는 것 찾기. 

        for item in table.select('tr:not(.title1)'):
            item = item.select('td span')  # item = span list 
            if item == []:                # block은 colon 
                continue 
            else:
                page_date = item[0].text
                if last_page_date > page_date:
                    last_page_date = page_date
                else:
                    stop_loop = True
                    break

                print(item[0].text)
                # 2021.06.18부터 2011.01.01 찾아보기
                result.append([num.text.strip() for num in item])

                if item[0].text == '2011.01.03':    
                    stop_loop = True    
                    break
                
        if (stop_loop):            # 이중반복문 out 
            break
result = pd.DataFrame(result, columns = ['date', 'close', 'diff', 'diff_rate',
                        'volume', ' int_dff', 'frgn_dff', 'frgn_share', 'frgn_rate'])
result.to_csv('data/frgn_invest_Top10.csv')