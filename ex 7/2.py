# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:03:17 2018

@author: user
"""

A =[[3, 5, 6],[4, 8, 10],[2, 1, 8]]
B =[[1, 0, 0],[0, 1, 0],[0, 0, 1]]
result =[[0, 0, 0],[0, 0, 0],[0, 0, 0]]
for i in range(len(A)):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]
for r in result:
    print(r)