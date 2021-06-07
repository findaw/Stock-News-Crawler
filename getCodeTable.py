import pandas as pd
import numpy as np

code_table = pd.read_csv('data/krx_code.csv')
code_table[['단축코드', '한글 종목명']]
code_table['단축코드'] = code_table['단축코드'].apply(pd.to_numeric, errors='coerce')
rate_best_data = pd.read_csv('data/급등주포착.csv', index_col=[0])
rate_best_data.head(5)
data = pd.merge(rate_best_data, code_table[['단축코드','한글 종목명']], how='left', left_on=['code'], right_on=['단축코드'], sort=True)
data.to_csv('data/급등주포착_최종.csv')



