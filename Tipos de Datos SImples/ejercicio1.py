#!/usr/bin/env python3

import numpy as np
import pandas
from sklearn import linear_model
import matplotlib.pyplot as plt
from scipy import stats

df = pandas.read_csv("data.csv") 

x = df[['Weight']]
y = df['CO2']         

regr = linear_model.LinearRegression()

regr.fit(x, y)

"""
pred = regr.predict(x)

plt.scatter(x, y)

plt.plot(x, pred)

plt.show()
"""

