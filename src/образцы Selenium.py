#Поиск текста внутри обределенного блока и клик по нему:
    driver.find_element(By.XPATH,"//div[@class='more' and text()='More']").click()
    
#Поиск ссылки и клик по ней:
    driver.find_element(By.XPATH,"//a[contains( text(),'Загрузить еще')]").click()


#Поиск всех элементов с определенным признаком:
    links = driver.find_elements(By.XPATH, "//div[contains(@class, 'name')]")
    ссылк содержит в адресе '/p/'
    links = driver.find_elements(By.XPATH, "//a[contains(@href, '/p/')]")

#Получение данных из массива объектов:
    for link in links:
        tmp = link.get_attribute("href")
        tmp = link.get_attribute('text')
        tmp = link.text
    
    for element in self.driver.find_elements_by_tag_name('img'):
       print element.text
       print element.tag_name
       print element.parent
       print element.location
       print element.size

#Замена переменной в запросе:	   
	varname = 'my string'
	driver.find_element_by_xpath("//*[contains(text(), '%s')]" % varname)  # option 1
	driver.find_element_by_xpath("//*[contains(text(), '{0}')]".format(varname))  # option 2
	
	mystrings = ['my first string','my second string','my third string']
	for x in mystrings:
		driver.find_element_by_xpath("//*[contains(text(), '%s')]" % x)