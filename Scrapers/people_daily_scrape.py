# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:02:05 2018

@author: Steven Morgan
"""

import os
import re
#import sys                         # Only necessary for Python 2
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

#reload(sys)                        # Only necessary for Python 2
#sys.setdefaultencoding('utf8')     # Only necessary for Python 2

os.chdir("C:/Users/sum410/Dropbox/PSU2018-2019/Fall2018/SODA502/Subnational_Corrpution")

# Initiate web driver
path_to_chromedriver = 'C:/Users/sum410/Desktop/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://search.people.com.cn/language/english/getResult.jsp'
browser.get(url)

search_bar = browser.find_element_by_css_selector("input[id='keyword']")
search_bar = browser.find_element_by_id('keyword')
search_bar.send_keys('corrupt' + '\n')

# Iterate through links (nested for loop)
for i in range(0,152): # number of search result pages
    
    elems = browser.find_elements_by_xpath("//a[@href]")
    elems = [x for x in elems if re.search('http://english.people.com.cn/n3/', str(x.get_attribute("href")))]
    print(len(elems))
    elems = elems[::2]
    #print([x.get_attribute("href") for x in elems])
    
    ### Access each link and scrape contents
    
    # Click next
    
    elm = browser.find_element_by_class_name('next')
    
    try:
        browser.find_element(By.XPATH, '//a[contains(text(), "Next")]').click()
    except:
        break




url = 'http://search.people.com.cn/language/english/getResult.jsp'
browser.get(url)

search_bar = browser.find_element_by_css_selector("input[id='keyword']")
search_bar = browser.find_element_by_id('keyword')
search_bar.send_keys('corruption' + '\n')
