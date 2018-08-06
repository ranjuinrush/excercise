# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:37:48 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import statistics as stat
#import collections

excel_file = 'C:/Users/user/.spyder-py3/rent_dataset.xlsx'
df = pd.read_excel(excel_file)
#print(df.head())

def best_fit(x, y):
    xbar = np.mean(x)
    ybar = np.mean(y)
    n = len(x)
    num = sum(xi * yi for xi, yi in zip(x, y)) - n * xbar * ybar
    den = sum(pow(xi,2) for xi in x) - n * pow(xbar, 2)
    b = num/den
    a = ybar - b * xbar
    print("bes fit line:\ny = {:.2f} + {:.2f}x".format(a,b))
    return a, b

print(df.describe())
print("median\t", stat.median(df['Rent'].tolist()))
print("mode\t", stat.mode(df['Rent'].tolist()))
print("coefficient of variance\t", (stat.stdev(df['Rent'])/stat.mean(df['Rent'])))
#print(collections.Counter(df['Rent']))

df1 = pd.Series(df['Rent']).value_counts().reset_index().sort_values('index').reset_index(drop=True)
df1.columns = ['Rent', 'Frequency']
df1['Cumulative Frequency'] = df1['Frequency'].cumsum()
print (df1)

'''
df1 = pd.Series(df['Rent']).value_counts().sort_index().reset_index().reset_index(drop=True)
df1.columns = ['Rent', 'Frequency']
df1['Cumulative Frequency'] = df1['Frequency'].cumsum()
print (df1)
'''

plt.figure()
df.plot.hist(alpha=0.5)
plt.xlabel("Rent")
#df1['Rent'].plot.hist(alpha = 0.5)
plt.show()

a, b = best_fit(df1['Rent'], df1['Frequency'])
plt.scatter(df1['Rent'],df1['Frequency'])
yfit = [a + b * xi for xi in df1['Rent']]
plt.plot(df1['Rent'], yfit)
plt.grid()
plt.show()