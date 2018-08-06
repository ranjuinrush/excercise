# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:29:30 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
path = r"C:\Users\user\Desktop\Niranjana\1 aug\rent_dataset.xlsx"
file = pd.read_excel(path, header=[0])
print(file)
count  = list()
sum = 0
count = {}
for i in file.index:
    sum += file['Rent'][i]
    count[i] = 0
    for j in file.index:
        if i==j:
            count[i] += 1
    print('Count of '+str(file['Rent'][i]+' : '+str(count[i])))
mean = sum/i
median  = i/2
top = 0
for i in file.index:
    if count[i]>top:
        top = i
mode = file['Rent'][top]
print(mean)
print(median)
print(mode)