#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import inv

# Gradient descent for linear regression y = wᵀx
# X: array of shape (n, 2) where each row is [x_i, 1]
# y: array of shape (n,)
# α: learning rate

def gradient_descent(X, y, α):
	n = len(y)
	# initialize parameter vector [w, b]
	w = np.array([[0.0], [0.0]])

	# compute cost J(w)
	def L(w):
		J = 0.0
		for xi, yi in zip(X, y):
			xi = xi.reshape(2,1)
			J += (w.T @ xi - yi)**2
		return J / (2 * n)

	# compute gradient ∇J(w)
	def ߜL(w):
		grad = np.zeros((2,1))
		for xi, yi in zip(X, y):
			xi = xi.reshape(2,1)
			grad += (w.T @ xi - yi) * xi
		return grad / n

	J_list = []
	for t in range(1000):
		J_curr = L(w)
		J_list.append(J_curr.flatten()[0])
		w = w - α * ߜL(w)

	return w, J_list

if __name__ == "__main__":
	# Example usage
	X = np.array([
		[1, 1],
		[2, 1],
		[3, 1],
		[4, 1]
	])
	y = np.array([2, 2, 3, 4])
	α = 0.1
	w, J_list = gradient_descent(X, y, α)
	print(f"Learned parameters: w = {w.T}")


	# Via Closed-form solution
	y = y.reshape(4,1)
	w = inv(X.T @ X) @ X.T @ y
	print( w )


	# Plot cost trajectory
	plt.figure()
	plt.plot(J_list)
	plt.xlabel('Iteration')
	plt.ylabel('Cost J')
	plt.title('Gradient Descent Convergence')

	# Plot data points and regression line
	plt.figure()
	plt.scatter(X[:,0], y, label='Data')
	# Extract slope and intercept
	slope, intercept = w.flatten()
	# Line endpoints
	x_vals = np.array([X[:,0].min(), X[:,0].max()])
	y_vals = slope * x_vals + intercept
	plt.plot(x_vals, y_vals, label='Fit Line')
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title('Linear Regression Fit')
	plt.legend()

	plt.show()

