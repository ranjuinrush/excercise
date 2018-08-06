# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 14:26:09 2018

@author: user
"""

import pandas as pd
import numpy as np



data=pd.read_csv(r"C:\Users\user\Desktop\Niranjana\exam 2\camera_1.csv")
df=pd.DataFrame(data)
print(df.describe())
print("-------------------")
print(df.loc[0])
print("-------------------")
print(df.dtypes)
print("-------------------")
print(df.describe())
s = pd.Series(['Price'])
print("-------------------")
print(df.Price.describe())
print("-------------------")
print(df['Model'].head(26))
print(df['Release date'].head(26))
print(df['Price'].head(26))
print("-------------------")


'''
import matplotlib.pyplot as plt
size=df["Price"]
#print(size)
weight=df["Zoom wide (W)"]
#print(weight)
plt.title("Price vs Zoom ")
plt.xlabel("zoom")
plt.ylabel("price")
plt.scatter(weight,size)'''