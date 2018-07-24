"""
Created on Mon Jul 23 19:41:57 2018

@author: user
"""
sum=0
num=input("Enter number to check:")
leng=len(num)
temp = int(num)
while temp > 0:
   digit = temp % 10
   sum += digit ** leng
   temp //= 10
if num == sum:
   print(num,"is an Armstrong number")
else:
   print(num,"is not an Armstrong number")