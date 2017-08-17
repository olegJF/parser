from bs4 import BeautifulSoup
import requests

s=requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0'}

URL = 'http://eneyfoto.in.ua/login/'
s.get(URL, headers=headers)

soup = BeautifulSoup(s.get(URL).text)
csrf = soup.find("input", value=True)["value"]
print(csrf)