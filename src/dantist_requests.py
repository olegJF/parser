# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup as BS
import time

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0',
           'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
    }
zip_code = '19703'
url = 'https://www.invisalign.com/find-a-doctor?zip='+zip_code+'&searchType=adult&QuerySource=TR2'
time.sleep(5)
req = session.get(url, headers=headers)
bsObj = BS(req.content)
data = bsObj.prettify()

handle = open('dantist_req.txt', "w")
handle.write(data)
handle.close() 
