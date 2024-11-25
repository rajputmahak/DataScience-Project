# -*- coding: utf-8 -*-
"""iris(logistic_regression).ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18iPl4bGZDkrGmrk8bxAh_UER_2s6mnr7
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

path='/content/IRIS.csv'
df=pd.read_csv(path)
df.head()

from sklearn import preprocessing
le=preprocessing.LabelEncoder()
df['species']=le.fit_transform(df['species'])
df.head()

x=df[['sepal_length','sepal_width','petal_length','petal_width']]
y=df['species']
print(x,y)

from sklearn.model_selection import train_test_split
x_train,x_test, y_train, y_test=train_test_split(x,y,test_size=0.2,random_state=0)
print(x_train)
print(x_test)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(x_train,y_train)
df=np.array([[5.1,3.5,1.4,0.2]])
y_pred=knn.predict(df)
print(y_pred)
print(df)

from sklearn.metrics import accuracy_score
y_pred=knn.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)

from sklearn.linear_model import LogisticRegression
logreg=LogisticRegression()
logreg.fit(x_train,y_train)
y_pred=logreg.predict(x_test)
print(y_pred)

from sklearn.metrics import accuracy_score
y_pred=logreg.predict(x_test)
accuracy=accuracy_score(y_test,y_pred)
print(accuracy)