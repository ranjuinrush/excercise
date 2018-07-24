# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:13:38 2018

@author: user
"""

d={'A':10,'B':20,'C':30}
print("Total sum of values in the dictionary:")
s=1
for key in d:
    s=s*d[key]
print(str(s))