# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:17:00 2018

@author: user
"""

filename=input("Enter file name: ")
for line in reversed(list(open(filename))):
    print(line.rstrip())