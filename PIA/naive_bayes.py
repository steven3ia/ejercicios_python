#!/usr/bin/env python3

from sklearn import datasets
from sklearn import metrics 
import pandas as pd 
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB 
import matplotlib.pyplot as plt

data = {
    'weather': ['Sunny', 'Sunny', 'Sunny', 'Rainy', 'Rainy', 'Rainy', 'Clear', 'Clear', 'Clear', 'Clear'],
    'temp': ['Hot', 'Cold', 'Hot', 'Hot', 'Cold', 'Cold', 'Hot', 'Hot', 'Cold', 'Cold'],
    'go_outside': ['Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'Yes', 'Yes', 'No', 'No']
}

# Map the values to numbers
map = {'Sunny': 2, 'Rainy': 1, 'Clear': 0,
            'Hot': 1, 'Cold': 0}

df = pd.DataFrame(data)

dummies = pd.get_dummies(df, columns=['weather', 'temp'])

"""
print(dummies)
print(dummies['go_outside'])
print(dummies.drop('go_outside', axis=1))
"""

y = dummies['go_outside']
X = dummies.drop('go_outside', axis=1)

# Create the model
model = GaussianNB()

# Split the data into testing and training data
train_X, test_X, train_y, test_y = train_test_split(X, y, test_size=.2)

# Fit the model
model.fit(X, y)

"""
accuracy = model.score(test_X, test_y)
print('Accuracy:', accuracy)
"""

# Get the score
print('Score: ', model.score(X, y))

# Make the prediction
prediction = model.predict([[map['Rainy'],map['Cold']]] )

print(prediction)

"""
print(f'It is {Sunny} and {Cold}. Go outside?')
print('Prediction: ', 'Yes' if value == 1 else 'No')
"""
