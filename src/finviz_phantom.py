# -*- coding: utf-8 -*-
import time
import codecs
from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://finviz.com/quote.ashx?t=SGH'
driver = webdriver.PhantomJS()
driver.get(url)
time.sleep(0.5)
tr = driver.find_elements(By.XPATH, "//table[contains(@class, 'snapshot-table2')]/tbody/tr[contains(@class, 'table-dark-row')]")
for e in tr:
    print(e.text) 
driver.quit()

    


# data = driver.page_source
# handle = codecs.open('finviz_ph.html', "w", 'utf-8')
# handle.write(data)
# handle.close()

