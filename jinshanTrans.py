import random
import requests

s = requests.Session()

class Dict:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0',
            'Referer': 'http://fy.iciba.com/',
            'contentType': 'application/x-www-form-urlencoded; charset=UTF-8'
        }
        self.url = 'http://fy.iciba.com/ajax.php?a=fy'
        self.base_config() 

    def base_config(self):
        """
        设置基本的参数，cookie
        """
        s.get('http://fy.iciba.com/')

    def translate(self,text_to_trans):
        i = text_to_trans
        data = {
            'f':'auto',
			't':'auto',
			'w':i
        }
        resp = s.post(self.url, headers=self.headers, data=data)
        return resp.json()


def JinshanTrans(content):
	dic = Dict()
	text = dic.translate(content)['content']['out']
	return text
