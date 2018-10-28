import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://exist.ua/price.aspx?wid=11356032&pa=0&sortType=1'
resp = session.get(url, headers=headers)

if resp.status_code == 200:
    bsObj = BS(resp.content, "html.parser")
data = bsObj.prettify()#.encode('utf8')
# print(str(url_id))
handle = codecs.open('exist_ua.html', "w", 'utf-8')
handle.write(str(data))
handle.close()
# data = str(groups)
# handle = codecs.open('bigmir_groups.html', "w", 'utf-8')
# handle.write(str(data))
# handle.close()