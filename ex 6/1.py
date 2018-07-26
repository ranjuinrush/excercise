# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:11:28 2018

@author: user
"""

a = (['Rhia',10,20,30,40,50],
           ['Alan',75,80,75,85,100],
           ['Smith',80,80,80,90,95])
b=''
for i in range(0,len(a)):
    for j in range(0,2):
        print(a[i][j])
a=list(a)
a[2]=list(['Sam',82,79,88,97,99])
print(a)
a[0][3]=95
print(a)
x=list([[73,80,85]])
a.extend(x)
print(a)