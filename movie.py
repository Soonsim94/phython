'''
filename : movie.py
'''
from urllib import request
from bs4 import BeautifulSoup
url = 'https://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key=f5eef3421c602c6cb7ea224104795888&targetDt=20221031'
target = request.urlopen(url)
soup = BeautifulSoup(target, 'json.parse')
print(target)