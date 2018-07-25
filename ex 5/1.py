# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 11:16:51 2018

@author: user
"""

s=input("Enter string:")
count = 0
vowels = set("aeiou")
for letter in s:
    if letter in vowels:
        count += 1
print("Count of the vowels is:")
print(count)