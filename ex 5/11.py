# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:15:10 2018

@author: user
"""

with open("test.txt") as f:
    with open("out.txt", "w") as f1:
        for line in f:
            f1.write(line)