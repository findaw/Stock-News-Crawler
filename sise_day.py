from bs4 import BeautifulSoup
import pandas as pd 
import requests 

#item_code = pd.read_csv('C:\bitcamp\프로젝트\Naver Finance\sise_market_sum.csv')
#print(item_code) 
#삼성전자의 일별 시세 url 가져오기
item_code = pd.read_csv('sise_market_sum.csv')['code']
# print(item_code)

result = []
for code in item_code:
    pre_data = []
    for page in range(1,120):
        url = f'https://finance.naver.com/item/sise_day.nhn?code={code}&page={page}'
        print(url)

        res = requests.get(url, headers={'user-agent': 'Mozilla/5.0'}) # 서버가 response message를 받은 변수 
        soup_data = BeautifulSoup(res.content,'html.parser') #tag handling 
        table = soup_data.findAll('tr')
        table = table[2:] #print(type(table[5])) # class'bs4.element.Tag  
        
        sise_row = []
        for row in table:
            # td - selectone 
            if row.select_one('tr > td:nth-child(1) > span') is None:
                continue
            date = row.select_one('tr > td:nth-child(1) > span').text.strip()
            close = row.select_one('tr > td:nth-child(2) > span').text.strip()
            diff = row.select_one('tr > td:nth-child(3) > span').text.strip()
            open = row.select_one('tr > td:nth-child(4) > span').text.strip()
            high = row.select_one('tr > td:nth-child(5) > span').text.strip()
            low = row.select_one('tr > td:nth-child(6) > span').text.strip()
            volume = row.select_one('tr > td:nth-child(7) > span').text.strip()
    
        
            sise_row = [code,date,close,diff,open,high,low,volume]
        
        if sise_row != pre_data:
            result.append(sise_row)
            pre_data = sise_row
        else:
            break


# result - dataframe 
result = pd.DataFrame(result, columns=['code','date','close','diff','open','high','low','volume'])

result.to_csv('sise_day.csv')
