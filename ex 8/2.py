# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:08:18 2018

@author: user
"""

rad=int(input("Enter the radius great than or equal to 0:"))
dic={}
k=1
while k<rad+1:
    dic[k]=3.142*(k**2)
    k=k+1
print(dic)
