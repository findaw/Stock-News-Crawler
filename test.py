import urllib.request
from bs4 import BeautifulSoup
from itertools import count 
import pandas as pd
import ssl
import datetime
def get_request_url(url, enc='utf-8'):
    context = ssl._create_unverified_context()
    req = urllib.request.Request(url)
    try:
        respose = urllib.request.urlopen(req, context=context)
        if respose.getcode() == 200:
            print("get_request_url : [%s] Url Request Success"% datetime.datetime.now())
            try:
                rcv = respose.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')    # 모든 사이트가 유니코드를 쓰진 않는다.
                print("[Error!] get_request_url : [%s] Http Unicode Decode Error "% datetime.datetime.now())
            return ret
    except Exception as e:
        print(e)
        print("[%s] Error for URL " % datetime.datetime.now())
def getPelicanaAdress(sido, result):
    c = 0
    bEnd = True                     # flag
    for page in count():            # count sido pages  
        context = ssl._create_unverified_context()
        url = "https://pelicana.co.kr/store/stroe_search.html?branch_name=&gu=&si=%s&page=%s" \
        %(urllib.parse.quote(sido), str(page+1))

        rcv_data = get_request_url(url)         # get <http.client.HTTPResponse object>
        soupData = BeautifulSoup(rcv_data, "html.parser")
        for j in range(1,11):       # list items (10)
            bEnd = False
            c += 1
            print(c)      
            try:
                items = soupData.find('table', {'class' : 'table mt20'}).find_all('tr')[j].text.strip().split('\n')
                address = items[1]
                result.append([items[0], address.split()[0], address.split()[1], address, items[-2].strip()])
            except IndexError as e:
                bEnd = True
            except Exception as e:
                print('[Error!] getPelicanaAdress : ', e)
        if(bEnd == True):
            return bEnd


sido_list = ['서울특별시','부산광역시','대구광역시','제주특별자치도','광주광역시','울산광역시','인천광역시','세종특별자치시','경기도','강원도','경상북도','경상남도','충청북도','충청남도','전라북도','전라남도','대전광역시']
result = []

print("페리카나 주소 크롤링 시작")
for sido in sido_list:
    getPelicanaAdress(sido, result)
print(result)
print(len(result))
perincana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'address', 'phone'))
perincana_table.head()
perincana_table.to_csv('python_study/data/perlicana2.csv', encoding='utf-8',index =True)                
print("페리카나 주소 크롤링 종료")