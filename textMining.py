import pandas as pd
# download java >= 1.9
# sys.version
# download JPype1-JPversion-cp{Pyversoin}-win_{winversion}.whl
# move file to cmd directory
# pip install JPype1-JPversion-cp{Pyversoin}-win_{winversion}.whl
# pip install konlpy

"""
[Issue] 
: SystemError: java.nio.file.InvalidPathException: Illegal char <*> at index 52:
: solution : https://stackoverflow.com/questions/65842567/systemerror-java-nio-file-invalidpathexception
"""


from konlpy.tag import Okt

df_data = pd.read_csv('data/현대차_네이버_뉴스목록_2020.12.20~2021.06.03.csv')
#print(df_data['title'])

text = df_data['title'][10]
okt = Okt()
print(text)
print(okt.normalize(text))  # 정규화 처리
print(okt.phrases(text))   # 어구 추출
print(okt.morphs(text))   #형태소 분석
print(okt.pos(text))     #형태소 분석(pos tagger)
print(okt.nouns(text))  #명사 추출 
