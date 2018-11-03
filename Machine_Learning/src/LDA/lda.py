#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" LINEAR DISCRIMINANT ANALYSIS (LDA)
    for discrimination of multivariate, multiclass datasets

    LDA is a generalization of Fisher's linear discriminant that finds a projection that minimizes the Fisher-Rao discriminant among multiple classes. This technique requires continuous input data and a priori known classes.

    ASSUMPTIONS:
    - For those familiar with MANOVA, the same assumptions apply here.
    - Independent variables are all normal across same levels of grouping variables (multivariate normality).
    - Covariances are equal across classes (homoscedasticity).
    - Samples are chosen independently.
    - Predictive power may decrease with increased correlations among predictor variables (multicollinearity).

    For a more thorough overview of LDA, consult McLachlan, 2004, or Google. :)

    Written by Jason Manley, Github: @jmmanley
"""

import numpy as np
from scipy.linalg import eigh


def lda(data, labels, d = None, classes = None):
    """ Run linear discriminant analysis on a given set of data and class labels

        INPUTS:

        data = nxm data matrix, where columns represent m features and rows represent n samples

        labels = nx1 vector of class labels for the given data

        d = desired dimensionality after projection. d <= cardinality(labels)-1

        classes = cardinality(labels)x1 of class names (as in labels)


        OUTPUTS:

        W = mxd projection matrix to reduced dimensional space, spanned by the top cardinality(labels)-1 generalized eigenvectors of S_b and S_w

        proj_data = nxd data after projection under W

        vals = eigenvalues corresponding to eigenvectors in columns of W

        mu_c = dxc matrix, where each column is the class mean after projection

        S_c = dxdxc matrix of covariance matrices after projection

    """

    # get shapes

    n, m = data.shape
    assert (n == labels.shape[0])

    classes = np.unique(labels)
    c = classes.shape[0]

    if d is None:
        d = c


    # compute overall means and variances
    mu = np.mean(data, axis=0).reshape((1,data.shape[1])) # overall sample mean

    S_b = np.zeros(m)
    S_w = np.zeros(m)

    for ci in range(c):
        idx  = np.asarray(np.where(labels == classes[ci]))
        n_i  = idx.shape[1]
        curr_data = np.squeeze(data[idx,:])
        mu_i = np.mean(curr_data, axis=0).reshape((1,data.shape[1])) # class sample mean
        dev  = curr_data - np.repeat(mu_i, n_i, axis=0) # deviation from mean

        S_b  = S_b + n_i * (mu_i - mu) * (mu_i - mu).T # between class variation
        S_w  = S_w + np.dot(dev.T, dev)


    # train the projection matrix
    vals, vecs = eigh(S_b, S_w)              # find generalized eigendecomposition
    idx        = np.flipud(np.argsort(vals)) # find top eigenvalues

    W          = vecs[:,idx[0:d]]            # retrieve projection matrix
    vals       = vals[idx[0:d]]              # retrieve corresponding eigenvalues


    # compute projections and resulting means / covariances
    proj_data = data.dot(W)

    mu_c = np.zeros((d, c))
    S_c  = np.zeros((d, d, c))

    for ci in range(c):
        idx  = np.where(labels == classes[ci])
        mu_c[:,ci]  = np.mean(np.squeeze(proj_data[idx,:]), axis=0)
        S_c[:,:,ci] = np.cov(np.squeeze(proj_data[idx,:]).T)

    return W, proj_data, vals, mu_c, S_c


if __name__ == "__main__":
    import matplotlib.pyplot as plt

    # generate random gaussian data of two classes
    n = 1000
    mean1 = np.array([10, 8])
    cov1  = np.array([[1, -0.9],[-0.9, 1]])
    class1 = np.random.multivariate_normal(mean1, cov1, n)
    theta = np.radians(20)
    c, s = np.cos(theta), np.sin(theta)
    R = np.array(((c,-s), (s, c)))
    class1 = class1.dot(R)
    mean2 = np.array([10, 11])
    cov2  = np.array([[1, 0.8],[0.8, 1]])
    class2 = np.random.multivariate_normal(mean2, cov2, n)

    alldata = np.concatenate((class1, class2))
    labels = np.concatenate((np.zeros((n,)), np.ones((n,))))

    W, proj_data, vals, mu_c, S_c = lda(alldata, labels, d=2)

    plt.figure()
    plt.scatter(class1[:,0], class1[:,1])
    plt.scatter(class2[:,0], class2[:,1])
    plt.title('original data')

    plt.figure()
    plt.scatter(proj_data[np.where(labels==0),0], proj_data[np.where(labels==0),1])
    plt.scatter(proj_data[np.where(labels==1),0], proj_data[np.where(labels==1),1])
    plt.title('lda projection')
    plt.draw()
    plt.show()
