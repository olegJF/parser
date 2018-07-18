import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

# session = requests.Session()
# headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'http://top.bigmir.net/report/16936420/'
# resp = session.get(url, headers=headers)


data = ''
handle = codecs.open('bigmir_.html','r', 'utf-8')
data = handle.read()
handle.close()
stat = {}
stat['bigmir'] = {}
stat['bigmir']['xls_url'] = url + '?ver=&format=xls'
if True: # resp.status_code == 200:
    # bsObj = BS(resp.content, "html.parser")
    bsObj = BS(data, "html.parser")
    tables = bsObj.find_all('table', attrs={'class':'small'})
    general_stat = tables[0]
    detail_stat = tables[1]
    raw_data = general_stat.find_all('tr')
    general = []
    for tr in raw_data:
        value = tr.find('td', attrs={'class':'text_right'}).text.replace('\n', '').strip()
        title = tr.find('td', attrs={'class':'large'}).text.replace('\n', '').strip()
        general.append({'title': title, 'value': value})
    stat['bigmir']['general'] = general
    detail = []
    raw_data = detail_stat.find_all('tr')
    size = len(raw_data)
    for i in range(1, size):
        tr = raw_data[i]
        v = tr.find_all('td', attrs={'class': False})
        # print(v)
        title = tr.find('td', attrs={'class':'large'}).text.replace('\n', '').strip()
        values = {}
        values['today'] = v[0].text.replace('\n', '').strip()
        if i < size - 1:
            values['1_day_ago'] = v[1].text.replace('\n', '').strip()
            values['2_days_ago'] = v[2].text.replace('\n', '').strip()
            values['7_days_ago'] = v[3].text.replace('\n', '').strip()
            values['30_days_ago'] = v[4].text.replace('\n', '').strip()
        detail.append({'title': title, 'values': values}) 
    stat['bigmir']['detail'] = detail

# data = bsObj.prettify()#.encode('utf8')
handle = codecs.open('bigmir_stat.txt', "w", 'utf-8')
handle.write(str(stat))
handle.close()
# data = str(groups)
# handle = codecs.open('bigmir_groups.txt', "w", 'utf-8')
# handle.write(str(data))
# handle.close()