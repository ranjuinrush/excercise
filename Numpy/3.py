# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 11:38:31 2018

@author: user
"""

from numpy import array
A = array([[1, 2, 3], [1, 2, 3]])
print(A)

C = A + A
print(C)

#multiply dot

# We need install numpy in order to import it
import numpy as np
 
# input two matrices
mat1 = np.array([[1, 6, 5],[3 ,4, 8],[2, 12, 3]])
mat2 = np.array([[3, 4, 6],[5, 6, 7],[6,56, 7]])
print(mat1)
print(mat2)
# This will return dot product
res = np.dot(mat1,mat2)
print("Dot product:") 
# print resulted matrix
print(res)


 
# input_array
arr1 = [2, 27, 2, 21, 23]
arr2 = [2, 3, 4, 5, 6]
print ("arr1         : ", arr1)
print ("arr2         : ", arr2)
 
# output_array
out = np.divide(arr1, arr2)
print ("\nOutput array : \n", out)