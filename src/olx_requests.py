# -*- coding: utf-8 -*-
# It's work!
import requests
from bs4 import BeautifulSoup as BS
import codecs

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://www.olx.ua/kiev/q-%D0%B1%D0%BE%D0%BB%D0%B3%D0%B0%D1%80%D0%BA%D0%B0-230/'
req = session.get(url, headers=headers)
bsObj = BS(req.content, "html.parser")
data = bsObj.prettify()
#data = bsObj.find('div', id="job-list").encode('cp1251')
handle = codecs.open('olx.html', "w", 'utf-8')
handle.write(str(data))
handle.close() 
