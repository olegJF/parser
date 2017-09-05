
from selenium import webdriver
import time
driver = webdriver.PhantomJS()
driver.get('http://manhattanbni.com/chapterlist.php?chapterName=manhattan&chapterCity=&chapterArea=&chapterMeetingDay=&chapterMeetingTime=')
time.sleep(3)
#print(driver.find_element_by_id('content').text)
data = driver.page_source
driver.close()
handle = open('man.html', "w")
handle.write(str(data.encode('utf8')))
handle.close() 
