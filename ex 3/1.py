# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 14:05:58 2018

@author: user
"""

a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])
print("Second Largest element is:",a[n-2])
print("After swapping")
temp=int(a[0])
a[0]=a[n-1]
a[n-1]=temp
print(a)