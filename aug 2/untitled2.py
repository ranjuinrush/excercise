# -*- coding: utf-8 -*-
"""
Created on Mon Aug  6 09:35:03 2018

@author: user
"""

from sklearn import linear_model
from sklearn import datasets
import pandas as pd

data = datasets.load_boston()
#print(data.feature_names)
df = pd.DataFrame(data.data, columns=data.feature_names)

target = pd.DataFrame(data.target, columns=['MEDV'])

X = df[['RM', 'PTRATIO', 'LSTAT']]
y = target['MEDV']

lm = linear_model.LinearRegression()

model = lm.fit(X,y)

predictions = lm.predict(X)
print("Row      RM    PTRATIO  LSTAT  Predicted Price")
for i in [9, 19, 29]:
    print(i, end='\t')
    for j in list(X):
        print(X.loc[i, j], end='\t')
    print(predictions[i])

print("R^2 = ", lm.score(X,y))


#print(list(X))