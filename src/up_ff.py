# -*- coding: utf-8 -*-
from selenium import webdriver
import time
from bs4 import BeautifulSoup as BS
# headers = { 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#     'Accept-Encoding':'gzip, deflate, sdch',
#     'Accept-Language':'en-US,en;q=0.8',
#     'Cache-Control':'max-age=0',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0' }
# 
# for key in headers:
#     webdriver.DesiredCapabilities.PHANTOMJS['phantomjs.page.customHeaders.{}'.format(key)] = headers[key]
#     

driver = webdriver.Chrome()
driver.get('http://realestate.mastersam.com.ua/head.php') #'https://www.upwork.com/o/jobs/browse/skill/website-development/'
#driver.set_window_size(1400,1000)

#time.sleep(5)

#driver.get_screenshot_as_file('screenshots.png')
#print(driver.page_source)
data = driver.page_source #.find_element_by_id('job-list')
# bsObj = BS(driver)
# data = bsObj.prettify()#.encode('utf8')
# data = bsObj.find('div', id="job-list").encode('cp1251')
handle = open('output.txt', "w")
handle.write(data.encode('utf8'))
handle.close()
# print(data.encode('utf8'))
driver.close()
