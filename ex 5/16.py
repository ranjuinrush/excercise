# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:16:40 2018

@author: user
"""

fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
    for line in f:
        l=line.title()
        print(l)