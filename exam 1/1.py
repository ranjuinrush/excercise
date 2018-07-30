# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 14:47:35 2018

@author: user
"""
str2=""
str=input("Enter the paragraph:" )
lis=str.split(".")
if len(lis)<4:
    print("Atleast 4 sentences required")
    exit
else:
    print(lis)
lis[len(lis)//2]="UST Global specializez in Healthcare,Retail & Consumer Goods,Banking and Financial services,Telecom,Media & Technology,Insurance,Transportation & Logistics and Manufacturing & Utilities "
print(lis)

count = 0
vowels = set("aeiouAEIOU")
for word in lis:
    for cha in word:
        if cha in vowels:
            count += 1
print("Count of the vowels is:")
print(count)
str1=str2.join(lis)
print(str1)
import re
count = 0
uppercase=0
lenght=0
splcha = set("!@#$%&*,.")
for word in lis:
    for cha in word:        
        lenght+=1
        if cha in splcha:
            count += 1
            if re.search("[A-Z]",str1):
                uppercase+=1
            
             
print("Count of the special char is:")
print(count)
print("Count of the upper case is:")
print(uppercase)
lowercase=lenght-uppercase
print("Count of the lower case is:")
print(lowercase)

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
        print(word)
        print(counts[word])
word_count(str1)

       
first = [lis[0]]
last = [lis[-1]]
middle = lis[1:-1]
print("   ")
print (last)
print (middle)
print (first)
