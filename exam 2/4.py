# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:04:11 2018

@author: user
"""
 
from numpy import zeros, newaxis
a = np.array([[1,2,3],[4,5,6]]) 
print(a)
print("The dimensions of the array is:"+str(a.shape))
b = a[:, :, newaxis]
print("New dimension is:"+str(b.shape))
print(b)

c = np.array([[5,5,5],[5,5,5]]) 
d=a+c
print(d)
e = np.array([[2,2,2],[2,2,2]]) 
d=a-e
print(d)
d=a*c
print(d)