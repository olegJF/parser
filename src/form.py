import requests
from bs4 import BeautifulSoup
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'referer':'http://eneyfoto.in.ua/login/'}
s=requests.Session()

URL = 'http://eneyfoto.in.ua/login/'
response = s.get(URL, headers=headers)

soup = BeautifulSoup(response.text)
csrf = soup.find("input", value=True)["value"]
print(csrf)
params = {}
params ['username'] = 'fenya_root'
params ['password'] = 'jabafenya'
params ['csrfmiddlewaretoken'] = csrf
response = s.post("http://eneyfoto.in.ua/login/", data=params, headers=headers)
data = response.text
print(data.encode('utf8'))