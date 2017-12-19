from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.PhantomJS()
driver.get('https://www.drv.gov.ua/portal/!cm_core.cm_index?option=ext_dvk&pid100=80&prejim=2')
time.sleep(0.5)
#print(driver.find_element_by_id('content').text)
data = driver.page_source
# links = driver.find_elements(By.XPATH, "//a[contains(@href, 'chapterdetails.php')]")
# chapter_links = []
# for link in links:
#     tmp = link.get_attribute("href")
#     chapter_links.append(tmp)
# time.sleep(0.5)
# 
# # Chapters detail
# url_chapter = chapter_links[0]
# driver.get(url_chapter)
# chapter_name=driver.find_element(By.XPATH,"//div[contains(@class, 'leftcol')]/div/h1").text
# # print(chapter_name)
# details=driver.find_elements(By.XPATH,"//div[contains(@class, 'leftcol')]/p")
# meeting_details = ''
# for i in details:
#     tmp = i.text
#     if tmp != '': meeting_details += tmp+'\n'
# 
# leadership=driver.find_elements(By.XPATH,"//div[contains(@class, 'roleslist')]/p")
# chapter_leadership = ''
# for i in leadership:
#     chapter_leadership += i.text+'\n'
# chapter_leadership = chapter_leadership.replace('Send Message', '')
# 
# links = driver.find_elements(By.XPATH, "//a[contains(@href, 'memberdetails.php')]")
# members_links = []
# for link in links:
#     tmp = link.get_attribute("href")
#     members_links.append(tmp)
#     
# # Members detail
# time.sleep(0.5)
# url_member = members_links[0]
# driver.get(url_member)
# member_info=(driver.find_element(By.XPATH,"//div[contains(@class, 'company')]").text).split('\n')
# 
# member_name = member_info[0]
# # member_name=driver.find_element(By.XPATH,"//div[contains(@class, 'company')]/table/tbody/tr/td/h1").text
# details=driver.find_elements(By.XPATH,"//div[contains(@class, 'leftcol')]/p")
# contacts = ''
# for i in details:
#     tmp = i.text
#     if tmp != '': contacts += tmp+'\n'
#     
# contacts = contacts.replace('Send Message', '')
# 
# details=driver.find_elements(By.XPATH,"//div[contains(@class, 'leftcol')]/div/p")
# adress = ''
# for i in details:
#     tmp = i.text
#     if tmp != '': adress += tmp+'\n'
# 
# data = chapter_name + '\n' + meeting_details + chapter_leadership 
# data +='\n\n\t' + member_name+'\t'+contacts+'\t'+adress
#     
driver.close()
driver.quit()
handle = open('drv.txt', "w")
handle.write(data)
# handle.write(str(data.encode('utf8')))
handle.close() 
