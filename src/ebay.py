import requests
from bs4 import BeautifulSoup as BS

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
url = 'http://www.ebay.com/itm/Samsung-Galaxy-S8-SM-G950U-64GB-Midnight-Black-Unlocked-Smartphone-/272708239633?epid=235346440&hash=item3f7ead8111:g:mOQAAOSwjRpZOXt9'
req = session.get(url, headers=headers)
bsObj = BS(req.content)
#data = bsObj.prettify()#.encode('utf8')
data = bsObj.find_all("span", attrs={"class": "notranslate"})
#data = bsObj.find_all(id="prcIsum")
for d in data:
    soup = BS(str(d))
    print(soup.get_text())
    print('\n******************************\n')

print(data)
#data = bsObj.find('div', id="job-list").encode('cp1251')
# handle = open('output.txt', "w")
# handle.write(str(data))
# handle.close() 
