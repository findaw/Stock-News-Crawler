import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm


"""
: download java >= 1.9
: sys.version
: download JPype1-JPversion-cp{Pyversoin}-win_{winversion}.whl
: move file to cmd directory
: pip install JPype1-JPversion-cp{Pyversoin}-win_{winversion}.whl
: pip install konlpy

[Issue] 
: SystemError: java.nio.file.InvalidPathException: Illegal char <*> at index 52:
: solution : https://stackoverflow.com/questions/65842567/systemerror-java-nio-file-invalidpathexception
"""

from konlpy.tag import Okt
import nltk         # natural language tool kit
from nltk import tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer   # 사전 기반 감성 분석툴
#nltk.download('punkt')
#nltk.download('vader_lexicon')

df_data = pd.read_csv('data/현대차_네이버_뉴스목록_2020.12.20~2021.06.03.csv')
#print(df_data['title'])

text_list = df_data['content']   #Series
print(text_list)    


text = df_data['content'][10]
okt = Okt()
print(text)
print(okt.normalize(text))  # 정규화 처리
print(okt.phrases(text))   # 어구 추출
print(okt.morphs(text))   #형태소 분석
print(okt.pos(text))     #형태소 분석(pos tagger)
print(okt.nouns(text))  #명사 추출 
nouns = okt.nouns(text)
words = nltk.Text(okt.nouns(text))    # 단어를 문장으로 만들기
print(words) 
print(set(words.tokens))     # 중복단어 제거

words.vocab()    # 빈도수 체크 FreqDist객체에 담긴다.

plt.figure(figsize=(12,7))
# Plot 한글 글꼴 처리
path = 'C:\Windows\Fonts\malgunbd.ttf'
font_name = fm.FontProperties(fname=path).get_name()
print(font_name)
plt.rc('font', family=font_name)
#words.plot()

# 불용어 처리
stopword=['이','는','은','저','데','근데', '그러나','그리고','는데','하는데','한데','가','저']

words2 = [i for i in words if i not in stopword]
for txt in words2:
    print(txt)

print(text)
# 연관있는 단어 추출
words.concordance('긍정')


# 사전 기반 감성 분석
lines_list = tokenize.sent_tokenize(text)    # 텍스트를 문장 단위로 자르기 
print(lines_list)
sid = SentimentIntensityAnalyzer()

for article in text_list:
    for sent in tokenize.sent_tokenize(article):
        ss = sid.polarity_scores(sent)   #문장을 단어별로 분석해서 문장의 pos(긍정)/neu(중립)/neg(부정)에 대한 점수및 종합 점수 계산
        
        print(article)
        print(ss['compound'], ss['pos'], ss['neg'], ss['neu'])
        print()
