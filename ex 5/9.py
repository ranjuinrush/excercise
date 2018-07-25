# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 12:14:30 2018

@author: user
"""

fname = input("Enter file name: ")
file3=open(fname,"a")
c=input("Enter string to append: \n");
file3.write("\n")
file3.write(c)
file3.close()
print("Contents of appended file:");
file4=open(fname,'r')
line1=file4.readline()
while(line1!=""):
    print(line1)
    line1=file4.readline()    
file4.close()
