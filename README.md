
## Python Web Scraping Project


### 수집/생성한 자료 목록
* 네이버 금융 코스피 시가총액 TOP 200 _(https://finance.naver.com/sise/sise_market_sum.nhn?&page=1)_
* TOP 200기업의 최대 5년간의 일별 시세 _(https://finance.naver.com/item/sise_day.nhn?code=005930&page=1)_
* 일일 급등/급락률 4% 이상만 모은 리스트
* 급등/급락 날짜의 뉴스 목록
* 일별 시세에 대한 차트 생성
* 뉴스 키워드를 뽑아 워드클라우드 생성


<hr/>

### 파일 설명
+ sise_market_sum.py<br/>
`sise_market_sum.csv` 생성

+ sise_pre.py<br/>
sise_day.csv => `sise_day_digit.csv` 생성

+ sise.py 실행<br/>
sise_day.digit.csv => `급등주포착.csv` 생성

+ getCodeTable.py <br/>
급등주포착.csv => `급등주포착_최종.csv` 생성<br/> 
sese_day_digit.csv => `sise_day_digit_name.csv` 생성

+ newsList.py<br/>
뉴스 목록 가져오기 

<hr/>

### 앞으로 구현할 추가 기능
- [ ] 뉴스 본문 추출
- [ ] 뉴스 데이터 전처리 및 워드 
- [ ] 클라우드 결과 개선
- [ ] 커스텀 캔들차트



