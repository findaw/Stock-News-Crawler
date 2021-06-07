
## Python 뉴스 본문 크롤링


### 수집/생성한 데이터 목록
* 네이버 금융 코스피 시가총액 TOP 200 _(https://finance.naver.com/sise/sise_market_sum.nhn?&page=1)_
* TOP 200기업의 최대 5년간의 일별 시세 _(https://finance.naver.com/item/sise_day.nhn?code=005930&page=1)_
* 일일 급등/급락률 4% 이상만 모은 리스트
* 급등/급락 날짜의 뉴스 목록
* 뉴스 키워드를 뽑아 워드클라우드 생성


<hr/>

### 파일 설명
+ sise_market_sum.py
> out : sise_market_sum.csv

+ sise_pre.py 실행
> in : sise_day.csv
> out : sise_day_digit.csv 

+ sise.py 실행
> in : sise_day.digit.csv
> out : 급등주포착.csv

+ getCodeTable.py 실행
> in : 급등주포착.csv
> out : 급등주포착_최종.csv



