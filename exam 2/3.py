# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 15:36:59 2018

@author: user
"""

import pandas as pd
data=pd.read_csv(r'C:\Users\user\Desktop\Niranjana\exam 2\bmi.csv')
print(data)
file=data.sort_values(by=['height'])
print('NAME: HEIGHT')
for i in range(0,5):
    print(file.iloc[i]['name'],file.iloc[i]['height'],'\n')
BMI=[]
for i in range(0,5):
    bmi=data.iloc[i]['weight']/((data.iloc[i]['height']/100)**2)
    BMI.append(bmi)
print(BMI)
data['BMI']=BMI
print(data)
file4=data.sort_values(by=["BMI"])


for i in range(0,5):
    if(file4.iloc[i]['BMI']<18.5):
        print(file4.iloc[i]["name"],'Underweight: Your BMI is less than 18.5')
    if(file4.iloc[i]['BMI']>18.5 and file4.iloc[i]['BMI']<24.9):
        print(file4.iloc[i]["name"],'Healthy weight: Your BMI is 18.5 to 24.9')
    if(file4.iloc[i]['BMI']>24.9):
        print(file4.iloc[i]['name'],'Overweight: Your BMI is 25 and above')
