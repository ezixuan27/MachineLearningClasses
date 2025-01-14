#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from scipy.integrate import simpson
import matplotlib as mpl

mpl.rcParams['savefig.directory'] = '/home/chieh/code/MachineLearningClasses/ML_2/1_multivariate_gaussian'

# Define the grid for x and y
x = np.linspace(-7, 7, 100)
y = np.linspace(-7, 7, 100)
x, y = np.meshgrid(x, y)
pos = np.dstack((x, y))  # Stack x and y into a (100, 100, 2) array

# Define the parameters for 4 Gaussians
means = [
    np.array([0, 0]),
    np.array([2, 2]), 
    np.array([-1.5, 1]),
    np.array([1, -2])  
]

covariances = [
    np.array([[2, 0], [0, 3]]),
    np.array([[2, 0], [0, 2]]),
    np.array([[1, 0], [0, 1]]),
    np.array([[1, 0], [0, 1]]) 
]

weights = [0.25, 0.25, 0.25, 0.25]  # Equal weights for each Gaussian

# Compute the PDF for each Gaussian
z = np.zeros_like(x)
for mean, cov, weight in zip(means, covariances, weights):
    rv = multivariate_normal(mean, cov)
    z += weight * rv.pdf(pos)

# Normalize the mixture distribution
dx = x[0, 1] - x[0, 0]  # Grid spacing in x
dy = y[1, 0] - y[0, 0]  # Grid spacing in y
total_volume = simpson(simpson(z, dx=dx, axis=0), dx=dy)  # Compute total volume
z_normalized = z / total_volume  # Normalize z

# Create the 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surface = ax.plot_surface(x, y, z_normalized, cmap='viridis', edgecolor='none')

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('A 2D complex distribution.')

# Show the plot
plt.tight_layout()
plt.show()


