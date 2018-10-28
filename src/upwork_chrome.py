# -*- coding: utf-8 -*-
import time
import codecs
from selenium.webdriver.common.by import By
from selenium import webdriver

url = 'https://www.upwork.com/o/jobs/browse/skill/website-development/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(2)
data = driver.page_source
handle = codecs.open('upwork_s.html', "w", 'utf-8')
handle.write(data)
handle.close()


driver.quit()

    



