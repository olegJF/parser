# -*- coding: utf-8 -*-
# It's work!
import requests
from bs4 import BeautifulSoup as BS
import codecs

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://ua.jooble.org/%d1%80%d0%b0%d0%b1%d0%be%d1%82%d0%b0-python/%d0%9a%d0%b8%d0%b5%d0%b2?date=0'
req = session.get(url, headers=headers)
bsObj = BS(req.content, "html.parser")
data = bsObj.prettify()
#data = bsObj.find('div', id="job-list").encode('cp1251')
handle = codecs.open('jooble.html', "w", 'utf-8')
handle.write(str(data))
handle.close() 
