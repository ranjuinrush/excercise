# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:35:46 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import math

df = pd.read_csv('C:/Users/user/.spyder-py3/headbrain.csv')
df.plot(kind = 'scatter', x = 'Head Size(cm^3)', y = 'Brain Weight(grams)', color = 'black')

sum1 = 0
sum2 = 0
meanX = df['Head Size(cm^3)'].mean()
meanY = df['Brain Weight(grams)'].mean()
for size, wt in zip(df['Head Size(cm^3)'], df['Brain Weight(grams)']):
    sum1 += (size-meanX) * (wt-meanY)
    sum2 += pow((size-df['Head Size(cm^3)'].mean()), 2)

b1 = sum1/sum2   
print("B1 = ", b1)
b0 = meanY - b1 * meanX
print("B0 = ", b0)

summation = 0
total = 0
for i, j in zip(df['Head Size(cm^3)'], df['Brain Weight(grams)']):
    ypred = b0 + b1 * i
    summation += pow((j - ypred), 2)
    total += pow((j - meanY), 2)

rmse = math.sqrt(summation/len(df))
print("Root Mean Squared Value = ", rmse)

r2 = 1 - (summation/total)
print("R^2 = ", r2)

ypredList = []
for i in df['Head Size(cm^3)']:
    ypredList.append(b0 + b1 * i)

sortedPredValues = sorted(ypredList)
dfMod = df.sort_values('Brain Weight(grams)')
#print(dfMod)
plt.plot(df['Head Size(cm^3)'], ypredList, color = 'red')