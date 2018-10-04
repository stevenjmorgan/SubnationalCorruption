# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 09:42:06 2018

@author: sum410
"""

from collections import Counter
mylist = ['A','A','B','C','D','E','D'] # this should be the list of url's (elems)
cnt = Counter(mylist)
new_list = ([k for k, v in cnt.items() if v > 1])
print(new_list)