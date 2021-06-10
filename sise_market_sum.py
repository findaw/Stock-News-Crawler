import requests
from bs4 import BeautifulSoup
import pandas as pd 
sosok = 0 
count = 0 
result = []
for page in range(1, 11):
    url = f'https://finance.naver.com/sise/sise_market_sum.nhn?sosok={sosok}&page={page}'
    orginal_url = 'https://finance.naver.com'
    res = requests.get(url)
    soup_data = BeautifulSoup(res.content,'html.parser')
    for item in soup_data.select('.type_2 tbody tr'): # only tr / css selector 
        try:
            for title in item.select('a.tltle'):   # class="center" [class 가 center이 아닌 td tag ]
                count+=1
                print('item_name = ',title.text) 
                print('종합정보 주소:', orginal_url + title['href'])
                code = title['href'][-6:]    # as you see that the code is start from the end till the sixth place 
                print('item_code =',code)
                sise_url = f'https://finance.naver.com/sise/sise_market_sum.nhn?code={code}'
                print('시세탭 주소:', sise_url)
                result.append([title.text, code, sise_url]) #list를 만들어서 result에 추가. 
        except:
            continue  
df = pd.DataFrame(result, columns=['title', 'code', 'sise_url'])  #리스트를 데이터 프레임으로 형 변환.
df.to_csv('data/sise_market_sum.csv', encoding='utf-8')