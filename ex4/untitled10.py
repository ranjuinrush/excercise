# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 17:45:00 2018

@author: user
"""
diction={}
for i in range(10):
    name=str(input("Enter the name:"))
    marks=str(input("Enter the marks:"))
    diction[name]=marks
import operator
sort=sorted(diction.items(),key=operator.itemgetter(1))
print("result")
print('("Name","Marks")')
print(sort)