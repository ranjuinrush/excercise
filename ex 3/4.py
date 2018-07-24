# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:04:13 2018

@author: user
"""

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
print(a[2],a[5])
for i in range(1,6):
    print(a[i-1])
print(a[-7])
a[1]='x'
a[4]='y'
print(a)
a.remove(a[4])
print(len(a))