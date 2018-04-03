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
url = 'https://www.work.ua/jobs-kyiv-python/?days=122'
req = session.get(url, headers=headers)
# handle = codecs.open('work.html','r', 'utf-8')
# cnt = handle.read()
# handle.close()
if req.status_code == 200:
    bsObj = BS(req.content, "html.parser")
    p = bsObj.find('ul', attrs={'class':'pagination'})
    # print ('p', p)
    jobs = []
    # data = bsObj.prettify()
    a_href = 'https://www.work.ua'
    list_of_div = bsObj.find_all('div', attrs={'class':'job-link'})
    # print(list_of_div[0].contents[5].contents[1].text)
    
    for div in list_of_div:
        company = ''
        h2 = div.find('h2')
        logo = div.find('div', attrs={'class':'logo-img'}).img['alt']
        if logo:
            company = logo
        # print('h2', a_href+h2.a['href'], h2.a['title'].split(',')[-1])
        # print('logo',  logo.img['alt'].encode('utf-8'))
        title = h2.a.text
        # print('desc',  div.p.text.encode('utf-8'))
        title_list = title.split(' ')
        if not any(word in stop_list for word in title_list):
            jobs.append({'href': a_href+div.a['href'], 
                            'title': h2.a['title'],
                            'descript': '<h4>'+company+'</h4>'+str(div.p.text)
                            })
    
content = '<h2> Work.ua</h2>'
for job in jobs:
    content += '<a href="{href}" target="_blank">{title}</a><br/><p>{descript}</p><br/>'.format(**job)
    content += '--------------<br/>'
data = template + content + end
handle = codecs.open('works.html', "w", 'utf-8')
handle.write(str(data))
handle.close() 
