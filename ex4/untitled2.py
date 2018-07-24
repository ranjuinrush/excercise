# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:48:24 2018

@author: user
"""

n = 3
d = dict(input("Enter the first dictionary contents:").split() for i in range(n))
print (d)

m = 3
e = dict(input("Enter the second dictionary contents:").split() for j in range(m))
print (e)
d.update(e)
print("Concatenated dictionary",d)