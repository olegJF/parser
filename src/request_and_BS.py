import requests
from bs4 import BeautifulSoup as BS
import codecs

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'http://2peasrefugees.boards.net/board/1' #'http://1artoftraining.freeforums.net/board/2'
resp = session.get(url, headers=headers)
bsObj = BS(resp.content, "html.parser")
data = bsObj.find("body")
# data = bsObj.prettify()#.encode('utf8')
#data = bsObj.find('div', id="job-list").encode('cp1251')
handle = codecs.open('board_content.txt', "w", 'utf-8')
handle.write(str(data.text))
handle.close() 
