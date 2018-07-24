# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:52:05 2018

@author: user
"""
list1=[]
x=int(input("Enter the number of items in list: "))
import random
for i in range(1,x+1):
    a=random.randint(1,21)
    list1.append(a)
print(list1)