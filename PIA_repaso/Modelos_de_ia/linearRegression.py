#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# DATASET AGE AND SPEED OF 14 CARS
# x_points = [5,7,8,7,2,17,2,9,4,11,12,9,6]
# y_points = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# Using np.random.randint (lowest integer, size=(int or tuple of ints))
x_points = np.random.randint(20, size=(14))
y_points = np.random.randint(120, size=(14))

# TEST DATA
# linspace generates 100 spaced points in the interval
x = np.linspace(x_points.min(), x_points.max(), 100)

# Calculate a linear least-squares regression for two sets of measurements.
# Parameters (x, y) Two sets of measurements. Both arrays should have the same length. 
# Pendiente (m): slope
# Condición inicial (y0): intercept
# Tasa de Ajuste promedio (r): r
# Coeficiente de determinación (r²): r ** 2
slope, intercept, r, p, std_err = stats.linregress(x_points, y_points)

# y = b + mx -> y = intercept + slope × x + error
def myFunc(x):
    return slope * x + intercept

# Get the prediction with the "test data"
# Predicted values for x
model = list(map(myFunc, x))

# Draw points
plt.scatter(x_points, y_points)

# Draw a line with x and the predicted values (model)
plt.plot(x, model)

# Indicate the axes and the title of the graph
plt.title("Linear regression with SciPy")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# Show the plot
plt.show()