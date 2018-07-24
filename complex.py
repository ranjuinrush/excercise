# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
a=int(input("Enter the year:"))
if (a%4)==0:
    if(a%100)==0:
        if(a%400)==0:
            print("Leap year")
        else: print("Not leap")  
    else:print("Leap year")
else: print("Not leap")   