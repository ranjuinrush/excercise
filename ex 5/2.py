# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:10:55 2018

@author: user
"""

s1=input("Enter first string:")
s2=input("Enter second string:")
a=list(set(s1)&set(s2))
print("The common letters are:")
for i in a:
    print(i)