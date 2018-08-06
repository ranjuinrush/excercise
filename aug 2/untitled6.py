# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:36:33 2018

@author: user
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
get_ipython().magic('matplotlib inline')
import seaborn as sb
import matplotlib.patches as mpatches
import datetime
sb.set_style("whitegrid")

excel_file = 'C:/Users/user/.spyder-py3/ca_result.xlsx'
df = pd.read_excel(excel_file, header = [0, 1])
df.head()


# In[72]:


df.reset_index(level = 0, inplace = True)
df.head()


# In[73]:


df.rename(columns={'index': 'Year'}, inplace=True)
df.head()


# In[74]:


df['Year']


# In[75]:


type(df['Group I']['Pass %'])


# In[76]:


type(df['Group I']['Pass %'][0])


# In[77]:


type(df['Group I']['Pass %'][1])


# In[78]:


df['Group I']['Pass %'].astype('float')


# In[80]:


X = np.arange(len(df))
plt.bar(X + 0.00, df['Group I']['Pass %'], color = 'b', width = 0.25, tick_label = df['Year'].astype('str'))
plt.bar(X + 0.25, df['Group II']['Pass %'], color = 'g', width = 0.25, tick_label = df['Year'].astype('str'))
plt.bar(X + 0.50, df['Both Group']['Pass %'], color = 'r', width = 0.25, tick_label = df['Year'].astype('str'))
blue_patch = mpatches.Patch(color='blue', label='Group I')
green_patch = mpatches.Patch(color='green', label='Group II')
red_patch = mpatches.Patch(color='red', label='Both Groups')
plt.legend(handles=[blue_patch, green_patch, red_patch])
plt.xlabel("Year")
plt.ylabel("Pass %")
plt.title("CA Results")
plt.xticks(rotation = "vertical")
plt.show()