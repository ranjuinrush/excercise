# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 15:12:04 2018

@author: user
"""

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
count=0
num=int(input("Enter the number to find occurance: "))
for i in a:
    if int(a[i-1])==num:
        count=count+1
print("The number of occurance is:",count)
for i in a:
    if int(a[i-1]%2==0):
        evenlar=a[i-1]
        el=1
        break
for i in a:
    if int(a[i-1]%2==1):
        oddlar=a[i-1]
        ol=1
        break
for i in a:
    if int(a[i-1])%2==0:
        if evenlar<int(a[i-1]):
            evenlar=a[i-1]
    else:
        if oddlar<int(a[i-1]):
            oddlar=a[i-1]
print(evenlar,oddlar)