#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

# Define the means and covariance matrices
mean1 = np.array([0, 0])  # Mean of the first Gaussian
cov1 = np.array([[0.5, 0], [0, 0.5]])  # Covariance matrix of the first Gaussian

mean2 = np.array([3, 3])  # Mean of the second Gaussian
cov2 = np.array([[0.5, 0], [0, 0.5]])  # Covariance matrix of the second Gaussian (small variance)

# Create a grid of points for plotting
x, y = np.mgrid[-2:2:0.1, -2:2:0.1]  # Grid from -5 to 5 with step size 0.1
pos1 = np.dstack((x, y))  # Stack x and y to create a (x, y) position grid

# Create a grid of points for plotting
x2, y2 = np.mgrid[1:5:0.1, 1:5:0.1]  # Grid from -5 to 5 with step size 0.1
pos2 = np.dstack((x2, y2))  # Stack x and y to create a (x, y) position grid



# Create the multivariate Gaussian distributions
rv1 = multivariate_normal(mean1, cov1)  # First Gaussian
rv2 = multivariate_normal(mean2, cov2)  # Second Gaussian

# Evaluate the PDFs on the grid
z1 = rv1.pdf(pos1)  # PDF of the first Gaussian
z2 = rv2.pdf(pos2)  # PDF of the second Gaussian

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the first Gaussian
ax.plot_surface(x, y, z1, cmap='viridis', alpha=0.7, label='Gaussian 1: Mean=[0, 0]')

# Plot the second Gaussian
ax.plot_surface(x2, y2, z2, cmap='plasma', alpha=0.7, label='Gaussian 2: Mean=[3, 3]')

# Add labels, title, and legend
ax.set_title('3D Gaussian Distributions')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Probability Density')

# Add a legend (requires a workaround for 3D plots)
#ax.legend()

# Show the plot
plt.tight_layout()
plt.show()
