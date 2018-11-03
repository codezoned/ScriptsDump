# Author: Abhinav Dhere (abhitechnical41[at]gmail.com) 
# Originally written as { Problem 1, Assignment 1, SM in AI (CSE 471) - 2017 IIIT Hyderabad }
# Perceptron based classification for MNIST database ; Options available - single update ; batchwise update; with or without margin
# Coded from scratch, dependency is only Numpy.
# Expects data in CSV files.

import numpy as np
import sys
import math
import time

def getConfMatrix(pLabels,labels):
    '''
    Obtain confusion matrix for the classification performed on test data.
    '''
    TN=0;FN=0;FP=0;TP=0;
    for id in pLabels.keys():
     #   print(id)
     #   print str(pLabels[id])+' '+str(labels[id])
        if pLabels[id]==0 and labels[id]==0:
            TN+=1
        elif pLabels[id]==0 and labels[id]==1:
            FN+=1
        elif pLabels[id]==1 and labels[id]==0:
            FP+=1
        elif pLabels[id]==1 and labels[id]==1:
            TP+=1
    confMat = np.array([[TN, FP],[FN,TP]])
    return confMat

def getStats(labelsP,labels):
    c = getConfMatrix(labelsP,labels)
    acc = (c[1,1]+c[0,0])/float(c[0,0]+c[0,1]+c[1,0]+c[1,1])
    recall = c[1,1]/float(c[1,1]+c[1,0])
    print("Accuracy: "+str(acc*100))
    print("Recall: "+str(recall*100))

def readFile(filename,datType):
    '''
    Read csv file specified by filename into two separate numpy arrays, one for features and one for header i.e. names of features.
    '''
    if datType==0:
        colNos = range(1,785)
        data = np.genfromtxt(filename,dtype=int,delimiter=',',autostrip=True,usecols=colNos)
        labels = np.genfromtxt(filename,dtype=int,delimiter=',',autostrip=True,usecols=[0])
        return data,labels
    elif datType==1:
        data = np.genfromtxt(filename,dtype=int,delimiter=',',autostrip=True)
        return data

def predict(w,x,i,margin):
    if (np.dot(np.transpose(w),x[i])>=margin):    
        pred = 1
    elif (np.dot(np.transpose(w),x[i])<margin):
        pred = 0
    return pred

def augment(data):
    aug = np.ones((data.shape[0],1))
    x = np.concatenate((aug,data),axis=1)
    return x

def train(data_train_file,method,margin):
    [data,labels] = readFile(data_train_file,0)
    x = augment(data)
    w = np.random.rand(x.shape[1])
    eta = 1
    #w = w + err*x[0,:]
    if method=='single':
        for i in range(x.shape[0]):
            predVal = predict(w,x,i,margin)
            err = labels[i]-predVal
            if err!=0:
                w = w + (err*eta)*x[i,:]
    elif method=='batch':
        z = [label if label==1 else -1 for label in labels]
        w = w + sum([z[num]*x[num] for num in range(x.shape[0])])
        lenValue = x.shape[0]
        oldDefaulters = range(x.shape[0])
        while(lenValue>1):
            defaulters = []
            for i in oldDefaulters:
                if (np.dot(np.transpose(w),z[i]*x[i])<=0):
                    defaulters.append(i)
            x_sum = sum([z[j]*x[j] for j in defaulters])
            w = w + eta*x_sum
            lenValue = len(defaulters)
            oldDefaulters = defaulters
    return w

def test(w,data_test_file,margin):
    data_test = readFile(data_test_file,1)
    x = augment(data_test)
    predVal = {}
    for i in range(data_test.shape[0]):
        predVal[i] = predict(w,x,i,margin)
    return predVal


def classify(trainFile,testFile,method,margin):
    w = train(data_train_file,method,margin)
    labels_pred = test(w,data_test_file,margin)
    #getStats(labels_pred,labels)
    for id in labels_pred.keys():
        print(labels_pred[id])

if __name__ == "__main__":
#    start_time = time.time()
    data_train_file = sys.argv[1]
    data_test_file = sys.argv[2]

# Single sample perceptron ==>    
    # Without margin
    classify(data_train_file,data_test_file,'single',0)
    # With margin
    classify(data_train_file,data_test_file,'single',6)
# Batch perceptron ==>
    #Without margin
    classify(data_train_file,data_test_file,'batch',0)
    #With margin
    classify(data_train_file,data_test_file,'batch',6)
#    print("--- %s seconds ---" % (time.time() - start_time))
