# -*- coding: utf-8 -*-
"""
Created on Thu Aug  9 16:51:45 2018

@author: user
"""

import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
import pandas as pd

df=pd.read_csv("employee_data.csv")
print(df.head())
x=df[['Worked Hours','Certification','Experience in years']]
y=df['Salary']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=.2)

lm=linear_model.LinearRegression()
model=lm.fit(x_train,y_train)
prediction=lm.predict(x_test)
plt.scatter(x_test['Experience in years'],prediction,color='red')
plt.scatter(x_test['Experience in years'],y_test,c='blue')