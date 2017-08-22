
from selenium import webdriver
import time
driver = webdriver.PhantomJS()
driver.get('https://www.instagram.com/explore/tags/instagram/')
time.sleep(3)
#print(driver.find_element_by_id('content').text)
data = driver.page_source
driver.close()
handle = open('output.txt', "w")
handle.write(str(data.encode('utf8')))
handle.close() 
