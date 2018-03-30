# -*- coding: utf-8 -*-
# It's work!
import requests
from bs4 import BeautifulSoup as BS
import codecs

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://djinni.co/jobs/?primary_keyword=Python&location=%D0%9A%D0%B8%D0%B5%D0%B2'
req = session.get(url, headers=headers)
bsObj = BS(req.content, "html.parser")
list_of_li = bsObj.find_all('li', attrs={'class':'list-jobs__item'})
for li in list_of_li:
    div = li.find('div', attrs={'class':'list-jobs__title'})
    # print('div', div.a['href'], div.a.text)
    div_description = li.find('div', attrs={'class':'list-jobs__description'})
    descr=div_description.p.text.encode('cp1251')
    print('descr',  str(descr.decode('cp1251')))
    # link = div.find('a')
    # print('a', link.text)
# data = bsObj.prettify()
# data = bsObj.find('div', id="job-list").encode('cp1251')
# handle = codecs.open('djinni.html', "w", 'utf-8')
# handle.write(str(data))
# handle.close() 
