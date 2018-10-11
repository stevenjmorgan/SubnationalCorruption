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
from bs4 import BeautifulSoup
import urllib.request
from collections import Counter
#import requests

#reload(sys)                        # Only necessary for Python 2
#sys.setdefaultencoding('utf8')     # Only necessary for Python 2

os.chdir("C:/Users/sum410/Dropbox/PSU2018-2019/Fall2018/SODA502/Subnational_Corruption/Corrupt_Files_Chinese")
#os.chdir('C:/Users/Steve/Dropbox/PSU2018-2019/Fall2018/SODA502/Subnational_Corruption')

# Initiate web driver
path_to_chromedriver = 'C:/Users/sum410/Desktop/chromedriver'
#path_to_chromedriver = 'C:/Users/Steve/Desktop/chromedriver'
browser = webdriver.Chrome(executable_path = path_to_chromedriver)

url = 'http://search.people.com.cn/cnpeople/news/getNewsResult.jsp'
browser.get(url)

search_bar = browser.find_element_by_css_selector("input[id='keyword']")
search_bar = browser.find_element_by_id('keyword')
search_bar.clear()
search_bar.send_keys(str(u'腐败') + '\n')

seed = 24519
random.seed(seed)
counter = 1000000

for i in range(0, 1000):
    try:
        browser.find_element(By.XPATH, '//a[contains(text(), "下一页")]').click()
    except:
        break
    time.sleep(12)

# Iterate through links (nested for loop)
for i in range(0, 12500): # number of search result pages 12500

    #if i % 5 == 1:
    time.sleep(5)

    elems = browser.find_elements_by_xpath("//a[@href]")
    #elems = [x for x in elems if re.search('http://english.people.com.cn/n3/|http://english.people.com.cn/n/', str(x.get_attribute("href")))]
    elems = [a.get_attribute('href') for a in elems]
    cnt = Counter(elems)
    #print(elems)
    elems = ([k for k, v in cnt.items() if v > 1]) # Getting two extraneous links
    elems = [x for x in elems if not re.search('search', x)]
    print(elems)

    print(len(elems))
    #elems = elems[::2] # this should probably be set
    #elems = [a.get_attribute('href') for a in elems]
    #print([x.get_attribute("href") for x in elems])
    #print(elems)

    ### Access each link and scrape contents
    for link in elems:

        counter += 1
        title = ''
        title2 = ''
        content_par = ''

        # Works but scales poorly; let's do this in bs4
        '''
        #browser.get(link.get_attribute('href')) # Go to document
        browser.get(link)

        try:
            title = browser.find_element_by_tag_name('h1').text.strip()
        except:
            pass

        try:
            content = browser.find_elements_by_class_name('desc')
            content2 = [x.text for x in content]
            content_par =  '\n'.join(content2)
        except:
            pass

        ### For each link, write to a .txt file
        fileName = "CorruptNews" +  str(counter) + ".txt"
        print(fileName)
        textFile = open(fileName, 'w')
        textFile.write(title)
        textFile.write('\n')
        textFile.write(content_par)
        textFile.close()
        browser.execute_script("window.history.go(-1)")
        '''

        try:
            resp = urllib.request.urlopen(link)
        except:
            pass

        try:
            soup = BeautifulSoup(resp, 'html.parser')
        except:
            pass

        try:
            title = soup.find('h1').get_text().strip()
        except:
            pass

        try:
            title2 = soup.find('h1').get_text().strip()
        except:
            pass

        try:
            pElems = soup.find_all('div', class_ = 'paragraph')
            pElems = soup.find_all('p')
            p_text = [x.get_text() for x in pElems]
            content_par = ' '.join(p_text)
        except:
            pass

        fileName = "CorruptNews" +  str(counter) + ".txt"
        print(fileName)
        textFile = open(fileName, 'w', encoding='utf-8')
        textFile.write(title)
        textFile.write('\n')
        if title != title2:
            textFile.write(title2)
            textFile.write('\n')
        textFile.write(content_par)
        textFile.close()


    # Click next
    try:
        browser.find_element(By.XPATH, '//a[contains(text(), "下一页")]').click()
    except:
        break
