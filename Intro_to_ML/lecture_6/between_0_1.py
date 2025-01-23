#!/usr/bin/env python

from sklearn.preprocessing import MinMaxScaler
import numpy as np

X = np.array([[3,0,400],[2,1,200],[2,2,500],[1,1,100]])
print(X)

scaler = MinMaxScaler()
X = scaler.fit_transform(X)
print(X)


