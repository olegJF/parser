# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/explore/tags/instagram/')
time.sleep(2)
##element = driver.find_element_by_tag_name('html')
##element.send_keys(Keys.END)
#print(driver.find_element_by_id('content').text)
driver.find_element(By.XPATH,"//a[contains( text(),'Загрузить еще')]").click()
for i in range(2):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    links = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")
    #print(links)
a_href = []
for link in links:
    tmp = link.get_attribute("href")
    a_href.append(tmp)
##data = driver.page_source
data = '\r\n'.join(a_href)
driver.close()
##handle = open('output.txt', "w")
##handle.write(str(data.encode('utf8')))
##handle.close() 
handle = open('links.txt', "w")
handle.write(str(data))
handle.close() 
