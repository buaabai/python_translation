import random
import requests

s = requests.Session()


class Dict:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Referer': 'https://www.bing.com/',
            'contentType': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        self.url = 'https://www.bing.com/ttranslate?&IG=892C6A8E6512459A992C14B46FDD2A51&IID=translator.5035.3'
        self.base_config()

    def base_config(self):
        """
        设置基本的参数，cookie
        """
        s.get('https://www.bing.com/')

    def translate(self,text_to_trans):
        i = text_to_trans
        data = {
            'text': i,
            'from': 'zh-CHS',
            'to': 'en'
        }
        resp = s.post(self.url, headers=self.headers, data=data)
        return resp.json()


def BingTrans(content):
	dic = Dict()
	text = dic.translate(content)['translationResponse']
	return text
