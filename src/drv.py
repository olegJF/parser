import requests
from bs4 import BeautifulSoup as BS

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'https://www.drv.gov.ua/portal/!cm_core.cm_index?option=ext_dvk&pid100=80&pf5242=800088&prejim=2'
req = session.get(url, headers=headers)
bsObj = BS(req.content)
data = bsObj.prettify()#.encode('utf8')
#data = bsObj.find('div', id="job-list").encode('cp1251')
handle = open('drv.html', "w")
handle.write(data)
handle.close() 
