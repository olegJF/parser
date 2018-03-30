# -*- coding: utf-8 -*-
import time
import codecs
from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://www.olx.ua/kiev/q-%D0%B1%D0%BE%D0%BB%D0%B3%D0%B0%D1%80%D0%BA%D0%B0-230/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(0.5)
# tr = driver.find_elements(By.XPATH, "//table[contains(@class, 'snapshot-table2')]/tbody/tr[contains(@class, 'table-dark-row')]")
# for e in tr:
#     print(e.text) 
data = driver.page_source
handle = codecs.open('olx.html', "w", 'utf-8')
handle.write(data)
handle.close()


driver.quit()

    



