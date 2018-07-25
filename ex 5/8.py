# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:13:39 2018

@author: user
"""

fname = input("Enter file name: ")
num_lines = 0
with open(fname, 'r') as f:
    for line in f:
        num_lines += 1
print("Number of lines:")
print(num_lines)