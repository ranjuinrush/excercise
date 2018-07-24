# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:17:25 2018

@author: user
"""

test_string=input("Enter string:")
l=[]
l=test_string.split()
wordfreq=[l.count(p) for p in l]
print(dict(zip(l,wordfreq)))