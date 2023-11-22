#!/usr/bin/env python3

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# pares de puntos utilizados para generar / entrenar el modelo
x_points = np.array([5, 7, 8, 7, 2, 17, 2, 9, 4, 11, 12, 9, 6])
y_points = np.array([99, 86, 87, 88, 111, 86, 103, 87, 94, 78, 77, 85, 86])

slope, intercept, r, p, std_err = stats.linregress(x_points, y_points)

print("Pendiente (m):......................", slope)
print("Condición inicial (y0):.............", intercept)
print("Tasa de Ajuste promedio (r):........", r)
print("Coeficiente de determinación (r²):..", r ** 2)

# m = (y-y0) / (x-x0)   -->
# (y-y0) = m(x-x0)      -->
# y = m(x-x0) + y0      -->  \x0=0
# f(x) = y = mx + y0

# generamos una función con la ecuación de la recta
def func(x):
    return slope * x + intercept

# array de puntos en X para dibujar la recta (""datos de testing"")
x = np.linspace(x_points.min(), x_points.max(), 100)

# obtenemos la predicción con los ""datos de testing""
model = list(map(func, x))

# grado 1 (recta)
model1 = np.poly1d(np.polyfit(x_points, y_points, 1))  

"""
# dibujamos por una lado los puntos
plt.scatter(x_points, y_points)
# y por otro lado la recta de previsión
plt.plot(x, model1(x))
#
plt.plot(x, model)
"""

plt.subplot(1, 2, 1)
# Dibujar los puntos de datos
plt.scatter(x_points, y_points)
# Dibujar la recta de regresión lineal model1
plt.plot(x, model1(x))
plt.title("Linear regression with model1")
plt.xlabel("X axis")
plt.ylabel("Y axis")

plt.subplot(1, 2, 2)
# Dibujar los puntos de datos
plt.scatter(x_points, y_points)
# Dibujar la recta de regresión lineal model
plt.plot(x, model)
plt.title("Linear regression with model")
plt.xlabel("X axis")
plt.ylabel("Y axis")

# desplegamos el gráfico
plt.show()
