# -*- coding: utf-8 -*-
"""Boston Linear Regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11W_2HniwSGF3lOUVnPaokQnHPhVx33cJ
"""

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("HousingData.csv")
df.head()

df.columns

df.shape

df.info()

df.isnull().sum()

df=df.dropna()

df.isnull().sum()

from sklearn.model_selection import train_test_split
x = df.drop('MEDV',axis=1)
y = df.MEDV

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30, random_state=42)

x_train

x_test

from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()

x_train = scalar.fit_transform(x_train)
x_test = scalar.transform(x_test)

from sklearn.linear_model import LinearRegression
r = LinearRegression(fit_intercept=True, copy_X=True, n_jobs=None,positive=False)

r.fit(x_train, y_train)

predictions = r.predict(x_test)

plt.scatter(y_test,predictions)
plt.xlabel("Y Test")
plt.ylabel("Predicted Y")

from sklearn import metrics


print("MSE",metrics.mean_squared_error(y_test,predictions))
print("MAS",metrics.mean_absolute_error(y_test,predictions))
print("RME",np.sqrt(metrics.mean_squared_error(y_test,predictions)))

