from collections import Counter
from typing import Type
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
from wordcloud import WordCloud


def save_wordcloud(data, file_name):


    try:
        wordcloud = WordCloud(width=2000, 
                        height=1200, 
                        font_path='c:/Windows/Fonts/malgun.ttf', 
                        background_color='white', min_font_size=8, 
                        max_font_size=100).generate_from_frequencies(dict(zip(data['키워드'], data['빈도수'])))

        plt.figure()
        plt.axis('off')
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.savefig(f'data/figure/keyword/{file_name}_워드클라우드.png')
        #plt.show()
    except TypeError as te:
        pass


if __name__ == '__main__':
    path_dir = os.getcwd() +'\data\\keyword'
    file_list = os.listdir(path_dir)
    print(file_list)
            
    for file_name in file_list:
        df_data = pd.read_csv(f'{path_dir}\\{file_name}', index_col=[0])
        code_name = file_name.split('_')[0]
        save_wordcloud(df_data, file_name)
