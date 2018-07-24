# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:38:37 2018

@author: user
"""

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)

x=[]
m=int(input("Enter number of elements:"))
for i in range(1,m+1):
    c=int(input("Enter element:"))
    x.append(c)
inter=[]
for value1 in a:
    for value2 in x:
        if value1==value2:
            inter.append(value1)
print(inter)
a.append(x)
for i in inter:
    a.remove(i)
print(str(a).replace("["," "))