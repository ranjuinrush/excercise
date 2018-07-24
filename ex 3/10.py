# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:20:47 2018

@author: user
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def sigma(numbers):
    sums = []
    total = 0
    for i in numbers:
        total += i
        sums.append(total)
    print (sums)

sigma(numbers)