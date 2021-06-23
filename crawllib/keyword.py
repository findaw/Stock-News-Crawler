from konlpy.tag import Okt
from collections import Counter
from pandas.core.frame import DataFrame

def get_keywords(data, filter_words :list , n=50) -> list:
    okt = Okt()
    text_list = data
    keyword_list = []
    if type(data) == DataFrame:
        text_list = data['content'].tolist()
        text_list +=  data['title'].tolist()

    stopwords = []
    with open('res/stopwords.txt', 'rt', encoding='UTF8') as f:
        stopwords = f.read().splitlines()

    def filter_keyword(text, func, filter_word, stopwords):
        word_list = func(text)
        stopwords += [*filter_word]
        return [i for i in word_list if i not in stopwords and len(i) > 1]

    def get_most_common(wlist, n=50):
        counter = Counter(wlist)
        total_sentence = counter.most_common(n)
        return total_sentence

    for func in [okt.phrases, okt.morphs, okt.nouns]:
        for i in range(len(text_list)):
            keyword_list += filter_keyword(text_list[i], func, filter_words, stopwords)
        result = get_most_common(keyword_list, n)
        print(result)
        yield result


   
def search_keyword(data, keyword, n=50) -> list:
    text_list = data['content'].tolist()
    text_list +=  data['title'].tolist()
    search_list = [text for text in text_list if keyword in text]
    print(search_list)
    return get_keywords(search_list, keyword, n)
