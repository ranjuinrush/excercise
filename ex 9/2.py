# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:15:08 2018

@author: user
"""

class Employee:
    def __init__(self):
        self.str1 = "Employee"
        print("I am an employee.")
        
class FullTime(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.str2 = "Full time"
        print("I am a full time employee.")
        
class PartTime(Employee):
    def __init__(self):
        Employee.__init__(self)
        self.str3 = "Part time"
        print("I am a part time employee.")
        
class Intern(FullTime, PartTime):
    def __init__(self):
        FullTime.__init__(self)
        PartTime.__init__(self)
        print("I am an intern.")
        
    def printStr(self):
        print(self.str2, self.str3)
    
        
obj = Intern()
obj.printStr()