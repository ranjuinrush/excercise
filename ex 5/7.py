# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:13:20 2018

@author: user
"""

fname = input("Enter file name: ")
 
num_words = 0
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        num_words += len(words)
print("Number of words:")
print(num_words)