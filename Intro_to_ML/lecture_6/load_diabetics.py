#!/usr/bin/env python

from sklearn.datasets import load_diabetes
import numpy as np


X, y = load_diabetes(return_X_y=True)
print(X.shape)
print(y.shape)

