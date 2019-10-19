import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Dataset
ds = pd.read_csv('Churn_Modelling.csv')
X = ds.iloc[:, 3:13].values
y = ds.iloc[:, 13].values


from sklearn.preprocessing import LabelEncoder, OneHotEncoder

# Encoding gender
labelencoder_X_2 = LabelEncoder()
X[:, 2] = labelencoder_X_2.fit_transform(X[:, 2])

# Encoding country categories
labelencoder_X_1 = LabelEncoder()
X[:, 1] = labelencoder_X_1.fit_transform(X[:, 1])
onehotencoder = OneHotEncoder(categorical_features=[1])
X = onehotencoder.fit_transform(X).toarray()
X = X[:, 1:]


# Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

# Training/testing
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2,
                                                    random_state=0)

# Making the neural network
import keras
from keras.models import Sequential
from keras.layers import Dense

clf = Sequential()
clf.add(Dense(input_shape = (X.shape[1],), units = 6, activation = 'relu'))
clf.add(Dense(units = 6, activation = 'relu'))
clf.add(Dense(units = 1, activation = 'sigmoid'))
clf.compile(optimizer = "adam", loss = "binary_crossentropy", metrics = ['accuracy'])
clf.fit(X_train, y_train, batch_size = 10, nb_epoch = 100)

# Predicting results
y_pred = clf.predict(X_test, batch_size = 10)
y_pred = (y_pred > 0.5)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
