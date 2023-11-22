#!/usr/bin/env python3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

# 
df = pd.read_csv("diabetes.csv")
df.shape()

"""
x = np.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)
y = np.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#
x_test = np.linspace(x.min(), x.max()).reshape(-1,1)

logr = linear_model.LogisticRegression()
logr.fit(x,y)

#
y_predict = logr.predict(x_test)

#print(logr.predict_proba(x_test)[:,1])
#print(logr.predict(x_test))

plt.scatter(x, y, color="blue")
plt.plot(x_test, logr.predict_proba(x_test)[:,1], color="green")
plt.axhline(.5, color="red")
plt.show()
"""