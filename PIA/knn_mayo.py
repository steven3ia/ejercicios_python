#!/usr/bin/env python3

from sklearn import datasets
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt1

iris = datasets.load_iris()

# Load the Iris dataset
X = iris.data
y = iris.target

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

knn = KNeighborsClassifier(n_neighbors = 6)
knn.fit(X_train, y_train)

# Iris data split
classes = {0:'setosa',1:'versicolor',2:'virginicia'}

# 
new_point = [[1,1,1,1],[4,3,1.3,0.2]]

# 
predict = knn.predict(new_point)

# Create a scatter plot to visualize the results
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_test, label='Test Data')
plt.scatter(np.array(new_point)[:, 0], np.array(new_point)[:, 1], c=predict, marker='x', label='Predicted')
plt.xlabel('Sepal Length')
plt.ylabel('Sepal Width')
plt.legend()
plt.show()
