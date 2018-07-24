# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:03:44 2018

@author: user
"""

d={'A':100,'B':200,'C':300}
print("Total sum of values in the dictionary:")
s=0
for key in d:
    s=s+d[key]
print(str(s))