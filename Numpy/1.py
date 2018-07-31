# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 10:00:05 2018

@author: user
"""

import numpy as np 

a = np.array([[1,2,3],[4,5,6]]) 
print("The dimensions of the array is:"+str(a.shape))
a.shape = (2,3) 
print (a)
b=np.reshape(a,(1,(2*3)))
print(b)
sum1=np.sum(a)
print("sum of elements:"+str(sum1))
mini=np.min(a)
print("Min of elements:"+str(mini))
ma=np.max(a)
print("Max of elements:"+str(ma))
