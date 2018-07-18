import requests
from bs4 import BeautifulSoup as BS
import codecs
import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()


def get_data_from_table(table):
    tab_titles = ['hits', 'visitors', 'hosts']
    nums = table.find_all('td', attrs={'class': 'num'})
    pers = table.find_all('td', attrs={'class': 'per'})
    title = table.find('td', attrs={'class': 'large'})
    title = title.text.replace('\n', '').strip()
    values = {}
    for i, key in  enumerate(tab_titles):
        numbers = nums[i].text.replace('\xa0', '').replace('\n', '').strip()
        percent = pers[i].text.replace('\n', '').strip()
        values[key] = {'value': numbers, 'percent': percent}
    return values, title
TIMESTAMP = datetime.today().strftime('%y-%m-%d_%H:%M')
session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 5.1; rv:47.0) Gecko/20100101 Firefox/47.0','Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'}
url = 'http://top.bigmir.net/report/16944555/tree?&period=1'

resp = session.get(url, headers=headers)

# handle = codecs.open('tables.html','r', 'utf-8')
# data = handle.read()
# handle.close()
stat = {}
stat['bigmir'] = {}
stat['bigmir'][TIMESTAMP] = {}

if resp.status_code == 200:
    resp = session.get(url, headers=headers)
    bsObj = BS(driver.page_source, "html.parser")
    tree_div = bsObj.find('div', attrs={'class':'domainsTree'})
    tables_first = tree_div.find_all('table', attrs={'class':'tab_pad'})
    for tab in tables_first:
        plus = tab.find('td', attrs={'class': 'wid9'})
        pluses.append(plus.div.img['id'])
    # print(pluses)
    driver.get(url)
    time.sleep(3)
    all_id = {}
    bsObj = BS(driver.page_source, "html.parser")
    main_div = bsObj.find('div', attrs={'class':'domainsTree'})
    tables_first = main_div.find_all('table', attrs={'class':'tab_pad'})
    print(len(tables_first))
    data = []
    for i, id in enumerate(pluses):
        tmp = {}
        tab = tables_first[i]
        values, title = get_data_from_table(tab)
        tmp['domain'] = title
        tmp['general'] = values
        driver.find_element_by_id(id).click() 
        time.sleep(10)
        bsObj = BS(driver.page_source, "html.parser")
        second_level_div = bsObj.find('div', attrs={'id':id.replace('bt', '')})
        tables_second = second_level_div.find_all('table', attrs={'class':'small'})
        print(len(tables_second))
        detail = []
        if tables_second:
            for table in tables_second:
                tmp_s = {}
                values, title = get_data_from_table(table)
                tmp_s['domain'] = title
                tmp_s['general'] = values
                detail.append(tmp_s)
        tmp['detail'] = detail   
        # div = driver.find_element_by_id(id.replace('bt', ''))
        # # tables = div.find_elements(By.XPATH, "//table[contains(@class, 'small')]")
        # divs = div.find_elements_by_tag_name('div')
        # all_id[id] = []
        # try:
        #     for d in divs:
        #         key = d.get_attribute("id")
        #         if key:
        #             all_id[id].append(key)
        # except:
        #     pass

       ##   for tab in tables:
        #     images = tab.find_elements(By.XPATH, "//td[contains(@class, 'large')]/div/img[(contains(@title, 'Развернуть'))]")
        #     all_id[id] = []
        #     for image in images:
        #         key = image.get_attribute("id")
        #         all_id[id].append(key)
        #     for sub_id in  all_id[id]:
        #         try:
        #             driver.find_element_by_id(sub_id).click()
        #         except:
        #             pass
        #             
        #         time.sleep(8) 
        data.append(tmp)
                
    # print(all_id)
    # bsObj = BS(data, "html.parser")
    # bsObj = BS(driver.page_source, "html.parser")
    # tree_div = bsObj.find('div', attrs={'class':'domainsTree'})
    # tables = tree_div.find_all('table', class_='tab_pad')
    # keys = []
    # tab_titles = ['hits', 'visitors', 'hosts']
    # # print(len(tables_first))
    # for tab in tables:
    #     classes = tab['class']
    #     print(classes)
    #     if 'small' not in tab['class'] and 'border_b' not in tab['class']:
    #         #print(tab)
    #         tr = tab.find('tr')
    #         nums = tr.find_all('td', attrs={'class': 'num'})
    #         pers = tr.find_all('td', attrs={'class': 'per'})
    #         title = tr.find('td', attrs={'class': 'large'})
    #         
    #         plus = ''
    #         id = ''
    #         try:
    #             is_plus = tr.find('td', attrs={'class': 'wid9'})
    #             plus = is_plus.find('img', attrs={'id': True})
    #             id = plus['id']
    #         except:
    #             pass
    #     
    #         tmp = {}
    #         for i, key in  enumerate(tab_titles):
    #             print('i', i)
    #             numbers = nums[i].text.replace('\xa0', '').replace('\n', '').strip()
    #             percent = pers[i].text.replace('\n', '').strip()
    #             tmp[key] = {'numbers': numbers, 'percent': percent}
    #         tmp['domain'] = title.text.replace('\n', '').strip()
    #         stat['bigmir']['general'][title.text.replace('\n', '').strip()] = tmp
    #         print(id)
    #         if id:
    #             div_second_lavel =  tree_div.find('div', attrs={'id': id.replace('bt', '')})
    #             tables_second = div_second_lavel.find_all('table', attrs={'class':'small'})
    #             print(len(tables_second))
        
    stat['bigmir'][TIMESTAMP]['data'] = data
    
# bsObj = BS(resp.content, "html.parser")
# data = bsObj.prettify()#.encode('utf8')
data = stat
handle = codecs.open('stat.txt', "w", 'utf-8')
handle.write(str(data))
handle.close()
# data = str(groups)
# handle = codecs.open('bigmir_groups.txt', "w", 'utf-8')
# handle.write(str(data))
# handle.close()
# time.sleep(15)
driver.close()