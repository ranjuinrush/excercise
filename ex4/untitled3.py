# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 16:57:22 2018

@author: user
"""

d={'A':1,'B':2,'C':3}
key=input("Enter key to check:")
if key in d.keys():
      print("Key is present and value of the key is:")
      print(d[key])
else:
      print("Key isn't present!")