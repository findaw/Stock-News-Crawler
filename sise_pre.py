import pandas as pd
####
# : sise 정보 데이터 프레임 전처리
sise_data = pd.read_csv('data/sise_day.csv', index_col=0)

#sise_data['date'] = pd.to_datetime(sise_data['date'])
sise_data.loc[:,'close':] = sise_data.loc[:,'close':].apply(lambda x:x.str.split(',').str.join('').astype(int))
sise_data.to_csv('data/sise_day_digit.csv')