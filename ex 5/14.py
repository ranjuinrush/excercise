# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:16:08 2018

@author: user
"""

name1 = input("Enter file to be read from: ")
name2 = input("Enter file to be appended to: ")
fin = open(name1, "r")
data2 = fin.read()
fin.close()
fout = open(name2, "a")
fout.write(data2)
fout.close()