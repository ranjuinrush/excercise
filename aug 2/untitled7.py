# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:37:04 2018

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


# In[2]:


list1 = [1.45, 2.20, 0.75, 1.23, 1.25, 1.25, 3.09, 1.99, 2.00, 0.78, 1.32, 2.25, 3.15, 3.85, 0.52, 0.99, 1.38, 1.75, 1.22, 1.75]


# In[6]:


df = pd.DataFrame(list1, columns = ['Price'])
df


# In[7]:


plt.figure()
df.plot.hist(alpha=0.5)