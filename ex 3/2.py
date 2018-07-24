# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:31:16 2018

@author: user
"""

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
#a.sort()
x=[]
m=int(input("Enter number of elements:"))
for i in range(1,m+1):
    c=int(input("Enter element:"))
    x.append(c)
#a.sort()
merged=a+x
merged.sort()
print(merged)