# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:40:19 2018

@author: user
"""

height=[]
weight=[]
bmi=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=float(input("Enter height:"))
    height.append(b)
   
    c=float(input("Enter weight:"))
    weight.append(c)
    
    d=c/(b*b)
    print(d)
height=tuple(height)
weight=tuple(weight) 
print(weight)
print(height)
#bmi=tuple(bmi)