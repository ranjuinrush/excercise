# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 16:15:07 2018

@author: user
"""

#multiple inheritance
print("MULTIPLE inheritance")
class Mammal():
    def __init__(self):
        self.str1 = "Warm blooded"
        print("Mammal")

class Animal:
    def __init__(self):
        self.str2 = "Wild"	
        print("Animal")

class Tiger(Mammal, Animal):
    def __init__(self): 
        Mammal.__init__(self)
        Animal.__init__(self)
        print("Tiger")
		
    def printStrs(self):
        print(self.str1, self.str2)
		

ob = Tiger()
ob.printStrs()
print()
                                                                                                                                                                                   
#multilevel inheritance
print("MULTILEVEL inheritance")
class Mammal:
    def __init__(self):
        self.str1 = "Warm blooded"
        print("Mammal")

class Animal(Mammal):
    def __init__(self):
        Mammal.__init__(self)
        self.str2 = "Wild"	
        print("Animal")

class Tiger(Animal):
    def __init__(self): 
        Animal.__init__(self)
        print("Tiger")
		
    def printStrs(self):
        print(self.str1, self.str2)
		

ob = Tiger()
ob.printStrs()
print()

#hierarchical inheritance
print("HIERARCHICAL inheritance")
class Animal:
    def __init__(self):
        self.str = "Wild"	
        print("Animal")

class Tiger(Animal):
        
    def __init__(self):
        Animal.__init__(self)
        print("Tiger")
		
    def printStrs(self):
        print(self.str)
		
class Bear(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Bear")
		
    def printStrs(self):
        print(self.str)

ob1 = Tiger()
ob1.printStrs()
print()

ob2 = Bear()
ob2.printStrs()
print()