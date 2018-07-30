# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 15:58:12 2018

@author: user
"""

diction={}
for i in range(10):
    name=str(input("Enter the name:"))
    marks=str(input("Enter the marks:"))
    diction[name]=marks
import operator
sort=sorted(diction.items(),key=operator.itemgetter(1))
print("result")
print('("Name","Marks")')
print(sort)

name1=[]
m1=[]
m2=[]
m3=[]
for i in range(0,2):
    name=input("Enter the name:")
    sub1=int(input("Enter marks of the first subject: "))
    sub2=int(input("Enter marks of the second subject: "))
    sub3=int(input("Enter marks of the third subject: "))
    name1=name1.append(name)
    m1=m1.append(sub1)
    m2=m2.append(sub2)
    m3=m3.append(sub3)
    
print(name1,m1,m2,m3)

avg=(sub1+sub2+sub3)/3
if(avg>=90):
    print("Grade: A+")
elif(avg>=80&avg<90):
    print("Grade: A")
elif(avg>=70&avg<80):
    print("Grade: B+")
elif(avg>=60&avg<70):
    print("Grade: B")
elif(avg>=50&avg<60):
    print("Grade: C")
else:
    print("Grade: D")