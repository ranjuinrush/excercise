# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:06:50 2018

@author: user
"""

l_range=int(input("Enter the lower range:"))
u_range=int(input("Enter the upper range:"))
for i in range(l_range,u_range+1):
    for j in range(2,i//2+1):
        if(i/j==j):
            print(i)
            x=i
            k=len(str(i))
            sum=0
            while i>0:
                dig=i%10
                sum=sum+dig
                i=i/10
            if sum<10:
                print(x)
            
            
        