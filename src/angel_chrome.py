# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://angel.co/companies')
time.sleep(3)
##element = driver.find_element_by_tag_name('html')
##element.send_keys(Keys.END)
#print(driver.find_element_by_id('content').text)

# links = driver.find_elements(By.XPATH, "//div[contains(@class, 'name')]")
# print(len(links))
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(1)
driver.find_element(By.XPATH,"//div[@class='more' and text()='More']").click()
#driver.find_element(By.XPATH,"//*[contains( text(),'More')]").click()

# links = driver.find_elements(By.XPATH, "//div[contains(@class, 'name')]")

for i in range(5):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(0.5)
    if driver.find_element(By.XPATH,"//div[contains( @class,'more')]"):
        print('Find more')
        try:
            driver.find_element(By.XPATH,"//div[@class='more' and text()='More']").click()
        except:
            print('exception', i)
    
    else: time.sleep(0.5)
    time.sleep(0.5)
time.sleep(1)    
links = driver.find_elements(By.XPATH, "//div[contains(@class, 'name')]")
print(len(links))
# a_href = []
# for link in links:
#     #tmp = link.get_attribute("href")
#     tmp = link.text
#     a_href.append(tmp)
    
##data = driver.page_source
# data = '\r\n'.join(a_href)
driver.quit()
##handle = open('output.txt', "w")
##handle.write(str(data.encode('utf8')))
##handle.close() 
# handle = open('companies.txt', "w")
# handle.write(str(a_href))
# handle.close() 
