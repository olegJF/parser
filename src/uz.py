import requests
from bs4 import BeautifulSoup as BS
import codecs
import time

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://booking.uz.gov.ua/?from=2210790&to=2200001&date=2018-08-07&time=00%3A00&url=train-list'
resp = session.get(url, headers=headers)
data = ''
if resp.status_code == 200:
    bsObj = BS(resp.content, "html.parser")
    # div = bsObj.find('div', attrs={'class': 'doublecol'})
    # list_a = div.find_all('a', attrs={'class':'large'})
    # domain = 'http://top.bigmir.net'
    # groups = []
    # 
    # if list_a:
    #     for a in list_a:
    #         groups.append({'url': domain+a['href'], 'title': a.text})
    #         urls_gr.append(domain+a['href'])
    # # urls_gr.append('http://top.bigmir.net/show/administrations/')        
    # if urls_gr:
    #     for u in range(40, len(urls_gr)):
    #         url_gr = urls_gr[u]
    #         # print(url_gr)
    #         for i in range(10):
    #             page_url = url_gr + '{}/'.format(i)
    #             time.sleep(3.0)
    #             print(time.time())
    #             resp = session.get(page_url, headers=headers)
    #             bsObj = BS(resp.content, "html.parser")
    #             if resp.status_code == 200:
    #                 list_td = bsObj.find_all('td', attrs={'class':'llink'})
    #                 if list_td:
    #                     for td in list_td:
    #                         links = td.a['href'].split('?')
    #                         if len(links) == 2:
    #                             link = links[1].replace('%3A%2F%2F', '://').replace('%2F', '/').lower().split('&')
    #                             id = link[0].replace('id=', '')
    #                             full_url = link[1].replace('url=', '').split('//')[-1]
    #                             url = full_url.replace('www.', '').split('/')[0]
    #                             url_id.append({'id': id, 'url': url})

data = bsObj.prettify()#.encode('utf8')
# print(str(url_id))
# data = str(url_id)
handle = codecs.open('uz.html', "w", 'utf-8')
handle.write(str(data))
handle.close()
# data = str(groups)
# handle = codecs.open('bigmir_groups.txt', "w", 'utf-8')
# handle.write(str(data))
# handle.close()