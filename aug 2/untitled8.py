# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:37:19 2018

@author: user
"""

import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')
import math
import numpy as np

temp = [14.2, 16.4, 11.9, 15.2, 18.5, 22.1, 19.4, 25.1]
sales = [215, 325, 185, 332, 406, 522, 412, 614]


# In[11]:


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

a, b = best_fit(temp, sales)
plt.scatter(temp, sales)
plt.xlabel("Temperature (in degrees Celsius)")
plt.ylabel("Sales of ice cream")
plt.title("Relation between temperature and sale of ice cream")
yfit = [a + b * xi for xi in temp]
plt.plot(temp, yfit)
plt.grid()
plt.show()