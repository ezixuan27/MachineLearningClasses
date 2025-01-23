#!/usr/bin/env python

import numpy as np
from sklearn.linear_model import LinearRegression
from numpy.linalg import inv

X = np.array([	[  4.,  -9.2], 
				[ -4.,  -6.], 
				[ 12., -10.], 
				[ -1., -16.]])

y = np.array( [	[ -5.],
				[ -9.],
				[  2.], 
				[-17.]])

Ⅱ = np.ones((4,1))
Φ = np.hstack((X,Ⅱ))

#	Closed form solution 
w = inv(Φ.T@Φ) @ Φ.T @ y
print(w)


print('Predicted labels vs True Labels Compared Side by Side')
print(np.hstack((Φ @ w, y)))


# ----------------- Using a library
reg = LinearRegression().fit(X, y)
print(reg.coef_)
print(reg.intercept_)

pred_y = reg.predict(X)
print('Predicted labels')
print(pred_y)

