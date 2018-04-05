# -*- coding: utf-8 -*-
# It's work!
import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

stop_list = ['Senior', 'Sr.']
template = '<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body>'
end = '</body></html>'


session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
base_url = 'https://kiev.hh.ua/search/vacancy?order_by=publication_time&text=python&area=115&enable_snippets=true&clusters=true&search_period=3&currency_code=UAH'
urls = []
urls.append(base_url)
jobs = []
a_href = 'https://www.work.ua'
req = session.get(base_url, headers=headers)
# handle = codecs.open('dou.html','r', 'utf-8')
# cnt = handle.read()
# handle.close()
if True: # req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    # bsObj = BS(cnt, "html.parser")
#     div = bsObj.find('div', attrs={'id':'vacancyListId'})
#     if div:
#         vacancy_list = div.find_all('li', attrs={'class':'l-vacancy'})
#         for v in vacancy_list:
#             # company = 'No name of company'
#             link = v.find('a', attrs={'class':'vt'})
#             title = link.text
#             firm = v.find('a', attrs={'class':'company'})
#             company = firm.text
#             desc = v.find('div', attrs={'class':'sh-info'})
#             title_list = title.split(' ')
#             if not any(word in stop_list for word in title_list):
#                 jobs.append({'href': link['href'], 
#                                 'title': title,
#                                 'descript':'<h4>'+company+'</h4>'+ str(desc.text)
#                                     })
# 
# content = '<h2> Rabota.ua</h2>'
# for job in jobs:
#     content += '<a href="{href}" target="_blank">{title}</a><br/><p>{descript}</p><br/>'.format(**job)
#     content += '--------------<br/><br/>'
# data = template + content + end

data = bsObj.prettify()

handle = codecs.open('hh.html', "w", 'utf-8')
handle.write(str(data))
handle.close() 
