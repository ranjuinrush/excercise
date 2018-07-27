# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:03:15 2018

@author: user
"""

import math
def armstrong(a):
    temp1 = a
    temp2 = a
    i=0
    sum = 0
    while(temp1>0):
        temp1 = int(temp1//10)
        i =i+1
    while(a>0):
        x = int(a%10)
        a = int(a//10)
        sum = sum + math.pow(x,i)
    if(sum == temp2): print(str(temp2)+' is an Armstrong Number')


for j in range(1,1000):
    armstrong(j)