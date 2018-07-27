# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:03:16 2018

@author: user
"""

n = input('Enter a String: ')

print('Length of String: ', len(n))

a=0
d=0
for i in  range(len(n)): 
    if n[i].isalpha(): a=a+1
    if n[i].isdigit(): d=d+1
print('Number of Charecters: '+str(a))
print('Number of Digits: '+str(d))