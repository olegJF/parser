# -*- coding: utf-8 -*-
# It's work!
import requests
from bs4 import BeautifulSoup as BS
import codecs
import datetime
import time

yesterday=datetime.date.today()-datetime.timedelta(1)
from_day = yesterday.strftime('%d.%m.%Y')

stop_list = ['Senior', 'Sr.']
template = '<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body>'
end = '</body></html>'

# handle = codecs.open('rabota.html','r', 'utf-8')
# cnt = handle.read()
# handle.close()

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
base_url = 'https://rabota.ua/jobsearch/vacancy_list?regionId=1&keyWords=Python&period=2&lastdate='+ from_day
urls = []
urls.append(base_url)
a_href = 'https://rabota.ua'
jobs = []
req = session.get(base_url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    dl = bsObj.find('dl', attrs={'id':'content_vacancyList_gridList_pagerInnerTable'})
    pages = dl.find_all('a', attrs={'class':'f-always-blue'})
    if pages:
        for p in pages:
            urls.append(a_href+p['href'])
else:
    jobs.append({'href': base_url, 
                    'title': 'rabota.ua - Page do not response',
                    'descript': ''
                        })
time.sleep(2)
for url in urls:
    req = session.get(url, headers=headers)
    time.sleep(2)
    if req.status_code == 200:
        bsObj = BS(req.content, "html.parser")
        table = bsObj.find('table', attrs={'id':'content_vacancyList_gridList'})
        if table:
            list_of_tr = table.find_all('tr', attrs={'id':True})
            for tr in list_of_tr:
                company = 'No name of company'
                h3 = tr.find('h3')
                title = h3.a.text
                logo = tr.find('p', attrs={'class':'f-vacancylist-companyname'})
                if logo:
                    company = logo.a.text
                posted = ''
                when_posted = tr.find('p', attrs={'class':'f-vacancylist-agotime'})
                if when_posted:
                    posted = when_posted.text
                descr = tr.find('p', attrs={'class':'f-vacancylist-shortdescr'}).text
                title_list = title.split(' ')
                if not any(word in stop_list for word in title_list):
                    jobs.append({'href': a_href+h3.a['href'], 
                                    'title': title+' , '+posted,
                                    'descript':'<h4>'+company+'</h4>'+ str(descr)
                                        })
        else:
            jobs.append({'href': url, 
                            'title': 'rabota.ua - The page is empty',
                            'descript': ''
                                })
    else:
        jobs.append({'href': url, 
                        'title': 'rabota.ua - Page do not response',
                        'descript': ''
                            })

content = '<h2> Rabota.ua</h2>'
for job in jobs:
    content += '<a href="{href}" target="_blank">{title}</a><br/><p>{descript}</p><br/>'.format(**job)
    content += '--------------<br/><br/>'
data = template + content + end
handle = codecs.open('rabotas.html', "w", 'utf-8')
handle.write(str(data))
handle.close() 
# https://rabota.ua/jobsearch/vacancy_list?regionId=1&keyWords=Python&period=2&lastdate=02.04.2018