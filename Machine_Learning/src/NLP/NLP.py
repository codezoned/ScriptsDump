"""
Created on Fri Apr  7 12:43:06 2017

@author: Robert
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-deep')

# Reading in data
ds = pd.read_csv('Restaurant_Reviews.tsv', sep = '\t', quoting = 3)

# Cleaning the text 
import re
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords

corpus = []

# Remove non-alphabetic characters, make everything lower case, 
# remove stopwords, append to corpus. 
for i in range(len(ds)):
   
    ps = PorterStemmer()
    review = re.sub('[^a-zA-Z]', ' ', ds['Review'][i])
    review = review.split()
    review = [ps.stem(w) for w in review if not w in set(stopwords.words('english'))]
    review = ' '.join(review)
    corpus.append(review)

# Bag of words
from sklearn.feature_extraction.text import CountVectorizer

cv = CountVectorizer(lowercase = True, 
                     max_features = 1500 )

X = cv.fit_transform(corpus).toarray()
y = ds['Liked'].values

# Classifying
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, accuracy_score
from sklearn.ensemble import RandomForestClassifier

X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2)

clf = RandomForestClassifier(n_estimators = 100, criterion = "entropy")
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
acc = accuracy_score(y_test, y_pred)


# Hadelin's challenge

from sklearn.naive_bayes import GaussianNB
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression

models = []
models.append(('Logistic regression', LogisticRegression()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('Random forest', RandomForestClassifier(n_estimators = 100, 
                                                       criterion = 'entropy')))
models.append(('NB', GaussianNB()))
models.append(('KernelSVM', SVC(kernel='rbf') ))

for name, model in models:
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    
    cm = confusion_matrix(y_test, y_pred)
    print ("---------- model: " + name + '-------------------')
    print("Acurracy: " + str(accuracy_score(y_test, y_pred)))
    TP, TN, FP, FN = cm[1][1], cm[0][0], cm[0][1], cm[1][0]
    precision = TP / (TP + FP)
    recall = TP / (TP + FN)
    F1 = 2* precision * recall/(precision+recall)
    print("Precision: " + str( round(precision,2)) )
    print("Recall: " + str(round(recall,2)) )
    print("F1: " + str(round(F1,2)))
