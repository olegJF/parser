# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as BS
import time

driver = webdriver.Chrome()
zip_code = '19703'
driver.get('https://www.invisalign.com/find-a-doctor?zip='+zip_code+'&searchType=adult&QuerySource=TR2')
time.sleep(5)
##element = driver.find_element_by_tag_name('html')
##element.send_keys(Keys.END)
#print(driver.find_element_by_id('content').text)
#element = driver.find_element(by=By.ID, value="dlResultList")
#elements = driver.find_elements(By.XPATH, "//div[contains(@class, 'doctor-desktop')]")
#elements = driver.find_elements(By.XPATH, "//div")
#bsObj = BS(driver.page_source)
data = driver.page_source
#div = bsObj.find( id="dlResultList")
#divs = bsObj.find_all("div", attrs={"class": "doctor-desktop"})
#text = div.prettify()
#print(div)
driver.close()
#print(divs)
##handle = open('output.txt', "w")
##handle.write(str(text.encode('utf8')))
##handle.close() 
handle = open('dantist.txt', "w")
handle.write(str(data.encode('utf8')))
handle.close() 
