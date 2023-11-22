#!/usr/bin/env python3

import pandas
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris


iris = load_iris()

dtree = DecisionTreeClassifier()
dtree = dtree.fit(iris.data, iris.target)

#plt.figure(figsize=(12, 8))
tree.plot_tree(dtree, filled=True, feature_names=iris.feature_names, class_names=iris.target_names)
plt.savefig("decision_tree.png", dpi=100)
plt.show()
