# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 17:02:05 2018

@author: sum410
"""

import os
import re
import sys
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

reload(sys)
sys.setdefaultencoding('utf8')

# Initiate web driver
path_to_chromedriver = 'C:/Users/sum410/Desktop/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://search.people.com.cn/language/english/getResult.jsp'
browser.get(url)

search_bar = browser.find_element_by_css_selector("input[id='keyword']")
search_bar = browser.find_element_by_id('keyword')
search_bar.send_keys('corrupt' + '\n')

# Iterate through links (nested for loop)


url = 'http://search.people.com.cn/language/english/getResult.jsp'
browser.get(url)

search_bar = browser.find_element_by_css_selector("input[id='keyword']")
search_bar = browser.find_element_by_id('keyword')
search_bar.send_keys('corruption' + '\n')
