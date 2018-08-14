# Written by Sagar Vakkala @ionicc

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model, metrics

# loading the dataset
data = datasets.load_boston(return_X_y=False)

# Creating a feature matrix X and a response vector Y
# Just in case: A vector is a 1D Array and a Matrix is an array with more than 1D
X = data.data
y = data.target

# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=1)

# Creating a linear regression object
reg = linear_model.LinearRegression()

# Training the model using the training sets
reg.fit(X_train, y_train)

# regression coefficients
print('Coefficients: \n', reg.coef_)

# We are aiming for a Variance score of 1 (Which means a perfect score)
print('Variance score: {}'.format(reg.score(X_test, y_test)))


## Setting up the plot style
plt.style.use('fivethirtyeight')

## Plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
            color = "green", s = 10, label = 'Train data')

## Plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
            color = "blue", s = 10, label = 'Test data')

## Plotting line for zero residual error
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2)

 ## Presenting the plot
plt.show()

##Great, You just made a LR Algorithm
