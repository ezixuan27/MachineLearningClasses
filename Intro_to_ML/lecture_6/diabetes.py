#!/usr/bin/env python

from sklearn.datasets import load_diabetes
from sklearn import preprocessing
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
import numpy as np


import os
import sys
if os.path.exists('/home/chieh/code/wPlotLib'):
	sys.path.insert(0,'/home/chieh/code/wPlotLib')
if os.path.exists('/home/chieh/code/wuML'):
	sys.path.insert(0,'/home/chieh/code/wuML')
import wuml


X,y = load_diabetes(return_X_y=True)
X = preprocessing.scale(X)

wuml.jupyter_print('\n\nRun all regressors sorted by least test error')
result = wuml.run_every_regressor(X, y=y, alpha=0.1, gamma=0.05, l1_ratio=0.05)
wuml.jupyter_print(result['Train/Test Summary'])
result['linear'].plot_feature_importance('linear Feature Importance', data.columns)

