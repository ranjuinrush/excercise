# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:15:44 2018

@author: user
"""

fname = input("Enter file name: ")
 
with open(fname, 'r') as f:
    for line in f:
        words = line.split()
        for i in words:
            for letter in i:
                if(letter.isdigit()):
                    print(letter)