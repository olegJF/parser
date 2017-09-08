from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.PhantomJS()
driver.get('http://www.colourlovers.com/palettes/most-loved/all-time/meta')

time.sleep(2)
links = driver.find_elements(By.XPATH, "//a[contains(@href, '/palette/')]")
color_links = []
for link in links:
    tmp = link.get_attribute("href")
    color_links.append(tmp)
time.sleep(0.5)

url=color_links[0]
driver.get(url)
palette_name=driver.find_element(By.XPATH,"//div[contains(@class, 'dark-bg-content-container')]/div/h1").text

colors = driver.find_elements(By.XPATH, "//div[contains(@class, 'detail-row')]/div[contains(@class, 'meta')]/div[not(contains(@class, 'right-col'))]/h4")
y = 0
components = ''
for color in colors:
    if y%2==0: components +='HEX:'+ color.text+'\n'
    else: components +='RGB:'+ color.text+'\n\n'
    y +=1

# print(driver.find_element_by_id('content').text)
# data = driver.page_source

data = palette_name+'\n' + 'Contains:\n'+components 
driver.quit()
handle = open('colourl.txt', "w")
handle.write(str(data.encode('utf8')))
handle.close() 
