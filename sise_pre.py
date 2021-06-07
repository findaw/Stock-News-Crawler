import pandas


import pandas as pd
####
# : sise 정보 데이터 프레임 전처리
#
sise_data = pd.read_csv('data/sise_day.csv')
sise_data = sise_data.drop(sise_data.columns[0], axis=1)
#sise_data.head(3)
#sise_data[sise_data['code']==51910].head(3)

#sise_data['date'] = pd.to_datetime(sise_data['date'])
sise_data['close'] = sise_data.close.str.split(',').str.join('').astype(int)
sise_data['diff'] = sise_data['diff'].str.split(',').str.join('').astype(int)
sise_data['open'] = sise_data.open.str.split(',').str.join('').astype(int)
sise_data['high'] = sise_data.high.str.split(',').str.join('').astype(int)
sise_data['low'] = sise_data.low.str.split(',').str.join('').astype(int)
sise_data['volume'] = sise_data.volume.str.split(',').str.join('').astype(int)

sise_data.to_csv('data/sise_day_digit.csv')