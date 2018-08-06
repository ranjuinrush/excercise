# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 15:13:46 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
from pandas.tools.plotting import table
import statistics,math

file = pd.read_csv(r'C:\Users\user\Desktop\Niranjana\pandas\train.csv') 
#print(file)


size=file["crim"]
#print(size)
weight=file['medv']
#print(weight)
plt.title("Affects of Crime Rate on Housing Price")
plt.xlabel("Per Capita Crime Rate")
plt.ylabel("Housing Rate")
plt.scatter(weight,size)
x = statistics.mean(size)
y = statistics.mean(weight)
b1=0
b2=0
for i in file.index:
    b1=b1+((size[i]-x)*(weight[i]-y))
    b2=b2+((size[i]-x)**2)
b1=b1/b2
print("B1:",b1)
b0=y-(b1*x)
print("B0:",b0)
yy=[]
y1=0
for i in file.index:
    y1=b0+(b1*size[i])
    yy.append(y1)
#print(yy)
#print(len(yy))
SSres=0
SStrt=0
for i in file.index:
    SSres=SSres+((weight[i]-yy[i])**2)
    SStrt=SStrt+((weight[i]-y)**2)
#print(SSres)
#print(SStrt)
rsq=1-(SSres/SStrt)
print("Rsquare=: ",rsq)
rms=math.sqrt(SSres/i)
print("RMS:",rms)

print("****SUMMARY STATISTICS********")
print(file.describe())