# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:22:08 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\user\Desktop\Niranjana\exam 2\100 Sales Records.csv")
df = pd.DataFrame(data)

print(df.columns)
print(data[0:10])

x = df['Region']
y = df['Total Revenue'].astype(float)
 
plt.hist(y)
plt.ylabel('Revenue')
plt.xlabel('Reigon')
plt.show()
print(df[df['Total Cost'] >= 1000000])
