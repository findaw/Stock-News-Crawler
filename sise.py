import pandas as pd

# : sise 정보 데이터 프레임 전처리
sise_data = pd.read_csv('data/sise_day_digit.csv')
sise_data = sise_data.drop(sise_data.columns[0], axis=1)
sise_data['date'] = pd.to_datetime(sise_data['date'])
sise_data.head()


####
# : 급상승한 종목과 날짜 추출
# 0 code / 1 date / 2 close / 3 diff /4 open / 5 high / 6 low / 7 volume
result = []
rate_best = 0.04      # 하루 4%
for code in set(sise_data.code):
    code_sise_data = sise_data[sise_data.code==code].values
    code_sise_data = code_sise_data[::-1]
    open_sise = 0
    print(len(code_sise_data))
    print(type(code_sise_data))
    for i in range(len(code_sise_data)-2, 0, -1):   # 전날 종가대비 오늘 종가 증가율(-4% or 4%)
        close_pre = code_sise_data[i-1][2]          # 전날 종가
        diff_day = code_sise_data[i][3]             # 증가 금액
        rate = diff_day /close_pre                  # 증가율
        if rate >= rate_best:
            # code date rate 전날종가 오늘종가 diff volume
            diff = code_sise_data[i][2] - code_sise_data[i-1][2]
            result.append([code, code_sise_data[i][1], rate, code_sise_data[i-1][2], code_sise_data[i][2], diff, code_sise_data[i][7]])

        
result = pd.DataFrame(result, columns=['code','date','rate', 'pre_close', 'close', 'diff', 'volume'])        
result.to_csv('data/급등주포착.csv')

# 전체평균 약 10일에 1번씩 +-4%의 등락율을 보인다








