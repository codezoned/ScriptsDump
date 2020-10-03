# Hierarchical Clustering
Used Hierarchical Clustering algortihm to cluster different segments of customers of a mall based on their income and expenditure.

## Understanding Clustering
Clustering is basically a technique that groups similar data points such that the points in the same group are more similar to each other than the points in the other groups. The group of similar data points is called a Cluster.

## Agglomerative Hierarchical clustering Technique
In this technique, initially each data point is considered as an individual cluster. At each iteration, the similar clusters merge with other clusters until one cluster or K clusters are formed.
The basic algorithm of Agglomerative is straight forward.
- Compute the proximity matrix
- Let each data point be a cluster
- Repeat: Merge the two closest clusters and update the proximity matrix
- Until only a single cluster remains
- Key operation is the computation of the proximity of two clusters

### Algorithm 
Step- 1: In the initial step, we calculate the proximity of individual points and consider all the data points as individual clusters.

Step- 2: In step two, similar clusters are merged together and formed as a single cluster. 

Step- 3: We again calculate the proximity of new clusters and merge the similar clusters to form new clusters.

Step- 4: Calculate the proximity of the new clusters. The similar clusters are merged together to form a new cluster.

Step- 5: Finally, all the clusters are merged together and form a single cluster.

### Dendogram
The Hierarchical clustering Technique can be visualized using a Dendrogram.
A Dendrogram is a tree-like diagram that records the sequences of merges or splits.

Here Hierarchical Clustering Technique has been applied on a sample dataset and the relevant dendogram & clustered data point graph have been included here.
*Hierarchical-Clustering.py* guides the entire hierarchical clustering approach along with data preprocessing and result generation. 
