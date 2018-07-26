# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 16:50:35 2018

@author: user
"""



punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

my_str = "#Python is an interpreted high level programming language for general-purpose programming *."
nopunct = ""
for char in my_str:
   if char not in punct:
       nopunct = nopunct + char

# display the unpunctuated string
print(nopunct)

def reverse(s):
    return s[::-1]
 
def isPalindrome(s):
    # Calling reverse function
    rev = reverse(s)
 
    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False
my_str=my_str.split()
for word in my_str:
    
    ans = isPalindrome(word)
    if ans == True:
        print(word)    
dic={}
for i in my_str:
    count = 0
    for j in my_str:
        if(i==j): count = count+1
    dic[i]=count
print(dic)