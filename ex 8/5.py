# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 09:57:24 2018

@author: user
"""

y=input("enter words, comma separated: ")
y=y.split(",")
y=sorted(y)
print (",".join(y))