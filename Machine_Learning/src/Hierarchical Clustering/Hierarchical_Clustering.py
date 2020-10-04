#Hierarchical Clustering

#Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing the mall dataset 
dataset = pd.read_csv('Mall_Customers.csv')
X = dataset.iloc[:,[3, 4]].values

#Using the dendogram to find the optimal number of clusters
import scipy.cluster.hierarchy  as sch
dendogram = sch.dendrogram(sch.linkage(X, method = 'ward'))# ward method minimizes within cluster variance
plt.title('Dendogram')
plt.xlabel('Customers')
plt.ylabel('Eucledian Distances')
plt.show()

#Fitting hierarchical clustering to the dataset
from sklearn.cluster import AgglomerativeClustering
hc = AgglomerativeClustering(n_clusters = 5, affinity = 'euclidean', linkage = 'ward')
y_hc = hc.fit_predict(X)

#Visualizing the clusters
plt.scatter(X[y_hc==0, 0], X[y_hc==0, 1], s = 100, c = 'red', label = 'Careful')
plt.scatter(X[y_hc==1, 0], X[y_hc==1, 1], s = 100, c = 'blue', label = 'Standard')
plt.scatter(X[y_hc==2, 0], X[y_hc==2, 1], s = 100, c = 'green', label = 'Target')
plt.scatter(X[y_hc==3, 0], X[y_hc==3, 1], s = 100, c = 'cyan', label = 'Careless')
plt.scatter(X[y_hc==4, 0], X[y_hc==4, 1], s = 100, c = 'magenta', label = 'Sensible')
plt.title('Cluster of Clients')
plt.xlabel('Annual Income(k$)')
plt.ylabel('Spending Score(1-100)')
plt.legend()
plt.show()
'''Analysing the graph
    RED - High income, low expenditure --> Careful
    BLUE - Average income, average expenditure --> Standard
    GREEN - High income, high expenditure --> Target
    CYAN - Low income, high expenditure --> Careless
    MAGENTA - Low income, low expenditure --> Sensible
   Changing the labels from Cluster"i" to the respective tags
'''