# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 09:03:16 2018

@author: user
"""

print('1) find the factorial')
print('2) find LCM')
print('3) find HCM')
print('4) factor of a number')
choice = int(input('Enter the choice: '))
if(choice == 1):
    a = int(input('Enter a Number to find Factorial of: '))
    fact = 1
    while(a>0):
        fact = fact*a;
        a = a-1
    print(str(fact)+' is the factorial')
elif(choice == 2):
    x = int(input('Enter 1 number: '))
    y = int(input('Enter 2 number: '))
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
    print(hcf)
elif(choice == 3):
    x = int(input('Enter 1 number: '))
    y = int(input('Enter 2 number: '))
    if x > y:
       greater = x
    else:
       greater = y
    while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1
    print(lcm)
elif(choice == 4):
    x = int(input('Enter number: '))
    print("The factors of",x,"are:")
    for i in range(1, x + 1):
       if x % i == 0:
           print(i)