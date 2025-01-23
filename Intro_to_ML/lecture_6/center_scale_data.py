#!/usr/bin/env python

from sklearn import preprocessing
import numpy as np

X = np.array([[3,0,400],[2,1,200],[2,2,500],[1,1,100]])
print(X)

X = preprocessing.scale(X)
print(X)

print(np.mean(X,axis=0))
print(np.std(X,axis=0))


