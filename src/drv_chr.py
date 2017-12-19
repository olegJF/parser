import csv
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://www.drv.gov.ua/portal/!cm_core.cm_index?option=ext_dvk&pid100=80&prejim=2')
# time.sleep(0.5)

info = driver.find_elements(By.XPATH, "//table[contains(@id, 'tab3')]/tbody/tr/td/a")
data = []
areas = ''
links_areas = []
u = []
for i,tmp in enumerate(info):
    
    link = tmp.get_attribute("href")
    disript = tmp.get_attribute("text").encode('cp1251')
    areas += 'link='+str(link) +'\t'+ 'disript:'+ str(disript)+'\n'
    u.append({'link':str(link),'disript': str(disript.decode('cp1251'))})
    links_areas.append(link)
    
FILENAME = "districts.csv"
with open(FILENAME, 'w', newline='') as file:
    columns = ["link", "disript"]
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
    writer.writeheader()
     
    writer.writerows(u)



# handle = open('areas.txt', "w")
# handle.write(areas)
# handle.close()


# tables = driver.find_elements(By.XPATH, "//table[contains(@id, 'tab3')]")
# link = 'https://www.drv.gov.ua/portal/!cm_core.cm_index?option=ext_dvk&pid100=80&pf3001=479&prejim=2'
all_districts = ''
# link = links_areas[0]
# driver.get(link)
# titles = driver.find_elements(By.XPATH, "//div[contains(@id, 'content')]/div[contains(@class, 'article')]/h3")
all = []

for link in links_areas:
    driver.get(link)
    titles = driver.find_elements(By.XPATH, "//div[contains(@id, 'content')]/div[contains(@class, 'article')]/h3")
    district = driver.find_element(By.XPATH, "//div[contains(@id, 'content')]/div[contains(@class, 'article')]/div[contains(@class, 'contentheading')]").text.encode('cp1251')
    all_districts += str(district)+'\n'
    all_districts += str(titles[1].text.encode('cp1251'))+'\n'
    title = str(titles[1].text.encode('cp1251'))
    all.append({'Number': str(district.decode('cp1251')), 'Area': '','Address':''})
    all.append({'Number': str('Звичайні виборчі дільниці:'), 'Area': '','Address':''})
    
    all_vd = driver.find_elements(By.XPATH, "//table[contains(@id, 'tab3')][1]/tbody/tr/td")
    i = 0
    while i < len(all_vd):
        num = all_vd[i+0].text.encode('cp1251')
        discr = all_vd[i+1].text.encode('cp1251')
        address = all_vd[i+2].text.encode('cp1251')
        i = i+5
        all_districts += 'Number: '+str(num)+'\t'+'Area : '+str(discr)+'\t'
        all_districts += 'Address: '+str(address)+'\n'
        all.append({'Number':int(num),'Area': str(discr.decode('cp1251')).replace(';','-'),'Address': str(address.decode('cp1251')).replace(';','-')})
    
    all_vd = driver.find_elements(By.XPATH, "//table[contains(@id, 'tab3')][2]/tbody/tr/td")
    all_districts += str(titles[2].text.encode('cp1251'))+'\n'
    title = str(titles[2].text.encode('cp1251'))+'\n'
    all.append({'Number': str('Спеціальні виборчі дільниці:'), 'Area': '','Address':''})
    i = 0
    while i < len(all_vd):
        num = all_vd[i+0].text.encode('cp1251')
        discr = all_vd[i+1].text.encode('cp1251')
        address = all_vd[i+2].text.encode('cp1251')
        i = i+4
        all_districts += 'Number: '+str(num)+'\t'+'Area : '+str(discr)+'\t'
        all_districts += 'Address: '+str(address)+'\n'
        all.append({'Number':int(num),'Area': str(discr.decode('cp1251')).replace(';','-'),'Address': str(address.decode('cp1251')).replace(';','-')})
    all_districts += '\n\n'

# handle = open('all_.txt', "w")
# handle.write(str(all))
# handle.close()

FILENAME = "all_areas.csv"


with open(FILENAME, 'w', newline='') as file:
    columns = ["Number", "Area", 'Address']
    writer = csv.DictWriter(file, fieldnames=columns, delimiter=';')
    writer.writeheader()
    writer.writerows(all)



# 
# handle = open('all_districts.txt', "w")
# handle.write(all_districts)
# handle.close()



driver.quit()
# handle = open('drv.txt', "w")
# handle.write(area)
# # handle.write(str(data.encode('utf8')))
# handle.close() 
