import http.client
import hashlib
from urllib import parse
import random

def BaiduTrans(content):
	appid = '20180402000142369'
	secretKey = 'HDzE4vG2cAtYKmICJbhA'
	httpClient = None
	myurl = '/api/trans/vip/translate'
	q = content
	fromLang = 'zh'
	toLang = 'en'
	salt = random.randint(32768, 65536)
	sign = appid+q+str(salt)+secretKey
	m1 = hashlib.md5()
	m1.update(sign.encode(encoding='utf-8'))
	sign = m1.hexdigest()
	myurl = myurl+'?appid='+appid+'&q='+parse.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign 

	#file = open('result.txt','w')
	try:
		httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
		httpClient.request('GET', myurl)
		response = httpClient.getresponse()
		Str = response.read().decode('utf-8')
		Str = eval(Str)
		#for line in str['trans_result']:
			#file.write(line['dst']+'\n')
	except Exception as e:
		print(e)
	finally:
		if httpClient:
			httpClient.close()
	#file.close()
	return Str['trans_result'][0]['dst']