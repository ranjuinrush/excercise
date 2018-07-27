# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:03:16 2018

@author: user
"""

n = int(input('Enter the number of terms: '))
dic={}
for i in range(1,(n+1)):
    dic[i]=i**2
print(dic)