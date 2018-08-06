# -*- coding: utf-8 -*-
"""
Created on Wed Aug  1 09:45:17 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt


file = pd.read_excel(r'C:\Users\user\Desktop\Niranjana\1 aug\ca_result.xlsx',header=[0,1]) 
print(file)
plt.hist([file['Group I']['Pass %'].astype(float),file['Group II']['Pass %'].astype(float),file['Both Group']['Pass %'].astype(float)],color=['red','green','yellow'])
plt.xticks(range(2013,2018))
plt.yticks(range(0,26))
plt.ylabel("Pass %")
plt.xlabel("Year")
plt.title("CA Results")