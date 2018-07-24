# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 08:50:37 2018

@author: user
"""

x=input("Enter the string: ")
ans=""
for i in range(len(x)):
    if i % 2 == 0:
      ans = ans + x[i]
print(ans)