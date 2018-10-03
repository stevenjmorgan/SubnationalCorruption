# -*- coding: utf-8 -*-

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
