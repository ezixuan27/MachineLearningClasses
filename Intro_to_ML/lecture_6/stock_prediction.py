#!/usr/bin/env python

import numpy as np
from numpy import ones
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from numpy import genfromtxt
from numpy import mean
from numpy.random import randn
import sys

#	these make printing nicer
np.set_printoptions(precision=4)
np.set_printoptions(threshold=30)
np.set_printoptions(linewidth=300)
np.set_printoptions(suppress=True)
np.set_printoptions(threshold=sys.maxsize)



X = genfromtxt('stock_prediction_data_scaled.csv', delimiter=',')
n = X.shape[0]
d = X.shape[1]
η = 0.001

y = genfromtxt('stock_price.csv', delimiter=',')
y = np.reshape(y, (n,1))

Ⅱ = ones((n,1))	# this is a column vector of 1s
Φ = np.hstack((X,Ⅱ))
w = randn(d+1,1)


mse_list = []
for i in range(20):
	fᑊ = Φ.T.dot(Φ.dot(w) - y)	# derivative in compact matrix form
	w = w - η*fᑊ				# gradient descent update w

	ε = (Φ.dot(w) - y)				# latest error
	mse = (ε.T.dot(ε)/n).item()		# item() extracts the number
	mse_list.append(mse)			# record mse

plt.plot(mse_list)
plt.title('MSE over GD')
plt.xlabel('steps')
plt.ylabel('MSE')


# Display the plot
plt.show()


# my stock price change prediction
ŷ = Φ.dot(w)
Y = np.hstack((ŷ, y))
print('Side by side comparison ŷ vs y') 
print(Y[0:20,:])
