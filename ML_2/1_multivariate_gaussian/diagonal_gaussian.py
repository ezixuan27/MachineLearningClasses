#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

mpl.rcParams['savefig.directory'] = '/home/chieh/code/MachineLearningClasses/ML_2/1_multivariate_gaussian'

def diagonal_gaussian(x, μ, σ):
	xₗ, xշ = x
	μₗ, μշ = μ
	σₗ, σշ = σ

	# Compute the exponent term
	exponent = -0.5 * (((xₗ - μₗ) ** 2 / σₗ ** 2) + ((xշ - μշ) ** 2 / σշ ** 2))
	
	# Compute the normalization constant
	normalization = 1 / (2 * np.pi * (σₗ*σշ))
	
	# Compute the probability density
	p = normalization * np.exp(exponent)
	return p


# Define the μ vector and Covariance matrix
μ = [0, 0]
σ = [1, 0.2]

# Create a grid of points in 2D space
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
pos = np.dstack((X, Y))  # Combine X and Y into a 2D grid

# Compute the multivariate Gaussian PDF at each point on the grid
Z = np.zeros_like(X)
for i in range(X.shape[0]):
	for j in range(X.shape[1]):
		#Z[i, j] = multivariate_gaussian(np.array([X[i, j], Y[i, j]]), μ, Σ)
		Z[i, j] = diagonal_gaussian(np.array([X[i, j], Y[i, j]]), μ, σ)

# Plot the 3D surface
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('2D Multivariate Gaussian Distribution')

# Add a color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10)

# Show the plot
plt.tight_layout()
plt.show()



