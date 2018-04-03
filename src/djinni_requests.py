# -*- coding: utf-8 -*-
# It's work!
import requests
from bs4 import BeautifulSoup as BS
import codecs

stop_list = ['Senior', 'Sr.']
template = '<!doctype html><html lang="en"><head><meta charset="utf-8"></head><body>'
end = '</body></html>'

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://djinni.co/jobs/?primary_keyword=Python&location=%D0%9A%D0%B8%D0%B5%D0%B2'
req = session.get(url, headers=headers)
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    jobs = []
    dj_href = 'https://djinni.co'
    list_of_li = bsObj.find_all('li', attrs={'class':'list-jobs__item'})
    for li in list_of_li:
        div = li.find('div', attrs={'class':'list-jobs__title'})
        # print('div', div.a['href'], div.a.text)
        div_description = li.find('div', attrs={'class':'list-jobs__description'})
        descr='No Discription!'
        title = div.a.text
        if div_description:
            descr=div_description.p.text
        title_list = title.split(' ')
        if not any(word in stop_list for word in title_list):
            jobs.append({'href': dj_href+div.a['href'], 
                            'title': title, 
                            'descript': str(descr)})
        # link = div.find('a')
        # print('a', link.text)
    # data = bsObj.prettify()
    # data = bsObj.find('div', id="job-list").encode('cp1251')
    
content = '<h2> Djinni</h2>'
for job in jobs:
    content += '<a href="{}" target="_blank">{}</a><br/><p>{}</p><br/>'.format(job['href'], job['title'], job['descript'])
    content += '--------------<br/>'
data = template + content + end
handle = codecs.open('djinni.html', "w", 'utf-8')
handle.write(str(data))
handle.close() 
