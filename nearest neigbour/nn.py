# -*- coding: utf-8 -*-
"""
Created on Mon Aug 13 09:57:11 2018

@author: user
"""

import numpy as np
import pandas as pd
import seaborn as sns
#sns.set_palette('husl')
import matplotlib.pyplot as plt

from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier
#from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv(r'Iris.csv')

data.head()
data.info()
data.describe()
data['Species'].value_counts()

tmp = data.drop('Id', axis=1)
g = sns.pairplot(tmp, hue='Species', markers='+')
plt.show()

X = data.drop(['Id', 'Species'], axis=1)
y = data['Species']
x_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)
# print(X.head())
print(X.shape)
# print(y.head())
print(y.shape)

# experimenting with different n values
k_range = list(range(1,26))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))
    
plt.plot(k_range, scores)
plt.xlabel('Value of k for KNN')
plt.ylabel('Accuracy Score')
plt.title('Accuracy Scores for Values of k of k-Nearest-Neighbors')
plt.show()