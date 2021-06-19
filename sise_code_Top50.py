import requests
from bs4 import BeautifulSoup
import pandas as pd 
count=0
result=[]
url =f'https://finance.naver.com/sise/sise_market_sum.nhn?sosok=0&page=1'
original_url = 'https://finance.naver.com'
res = requests.get(url)
soup_data = BeautifulSoup(res.content,'html.parser')     # BeautifulSoup으로 Html소스를 파이썬 객체로 반환하기 
for item in soup_data.select('.type_2 tbody tr'):    # class의 경우 .
    for title in item.select('td:not(.center) a'):         # if there's no center?
        count+=1
        print('item_name = ',title.text)
        code = title['href'][-6:]
        print('item_code =',code)
        frgn_url = f'https://finance.naver.com/item/frgn.nhn?code={code}'
        print('투자자탭 주소:',frgn_url)
        result.append([title.text, code, frgn_url])
df = pd.DataFrame(result, columns=['title', 'code', 'frgn_url'])
df.to_csv('data/sise_code_Top50.csv')