import requests 
from typing import Final
from requests.models import Response


class Crawler():
    Sort_Best : Final = 0
    Sort_Latest : Final = 1
    Sort_Oldest : Final = 2

    def __init__(self, url=''):
        self.url = url
        self.sort_type = Crawler.Sort_Best

    def get_url_data(self, url='') -> Response:
        if url == '':
            url = self.url
        headers = {'User-Agent' : 'Mozilla/5.0',}
        try:
            return requests.get(url, headers=headers)
        except requests.exceptions as re:
            print('[Error] : get_url_data')
            print(re)
            return False
    
    