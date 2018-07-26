# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 17:47:51 2018

@author: user
"""

n1 = {5, 3, 8, 6, 1}
n2 = {1, 5, 3, 4, 2}
union_list = list((n1) | (n2))
print(union_list)

inter_list = list((n1) & (n2))
print(inter_list)

diff_list = list((n1) - (n2))
print(diff_list)

maxi = max(union_list)
mini = min(union_list)
print(str(maxi)+' is the maximum element')
print(str(mini)+' is the minimum element')