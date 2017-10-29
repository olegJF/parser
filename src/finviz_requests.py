# -*- coding: utf-8 -*-
import requests
import codecs
from bs4 import BeautifulSoup as BS
from lxml import html

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://finviz.com/quote.ashx?t=SGH'
req = session.get(url, headers=headers)
##encoding = req.encoding if 'charset' in req.headers.get('content-type', '').lower() else None
bsObj = BS(req.content, 'html.parser') #, from_encoding=encoding)
table = bsObj.find_all('table', attrs={'class':'snapshot-table2'})[0]
tr = table.find_all('tr', attrs={'class':'table-dark-row'})[11]
volume = tr.find_all('td', attrs={'class':'snapshot-td2'})[4]
print (volume.text)
##data = bsObj.prettify()
###data = bsObj.find('div', id="job-list").encode('cp1251')
##handle = codecs.open('finviz.html', "w", 'utf-8')
##handle.write(data)
##handle.close()

