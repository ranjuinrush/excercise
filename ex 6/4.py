# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:55:21 2018

@author: user
"""

for x in range(900,1001):
    flag = 0
    for i in range(2,x//2):
        if x%i == 0: 
            flag=1
    if (flag==0):
        temp = str(x)
        rev = temp[::-1]
        if temp == rev:
            print("number is palindrome")
        else:
            print(" ")
        print(str(x) +' is Prime Number')