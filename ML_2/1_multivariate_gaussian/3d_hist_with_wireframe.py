#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Set random seed for reproducibility
np.random.seed(42)

# Generate random samples from 2D normal distribution
n_samples = 10000
mean = [0, 0]
cov = [[1, 0], [0, 1]]  # Standard normal distribution
samples = np.random.multivariate_normal(mean, cov, n_samples)

# Create the figure
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Create histogram
hist, xedges, yedges = np.histogram2d(samples[:, 0], samples[:, 1], bins=30, density=True)
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")

# Calculate centers of bins for wireframe
xcenters = (xedges[:-1] + xedges[1:]) / 2
ycenters = (yedges[:-1] + yedges[1:]) / 2
dx = xedges[1] - xedges[0]
dy = yedges[1] - yedges[0]

# Convert histogram data for bar3d
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0
dx = np.ones_like(xpos) * dx
dy = np.ones_like(ypos) * dy
dz = hist.ravel()

# Create bars with alpha transparency
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, alpha=0.2, color='skyblue')

# Create wireframe mesh
X, Y = np.meshgrid(np.linspace(-3, 3, 100), np.linspace(-3, 3, 100))
pos = np.dstack((X, Y))
rv = multivariate_normal(mean, cov)
Z = rv.pdf(pos)

# Plot wireframe
ax.plot_wireframe(X, Y, Z, color='red', alpha=0.5, linewidth=0.5)

# Customize the plot
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('3D Histogram with Gaussian Wireframe')

# Adjust the view
ax.view_init(elev=30, azim=45)
plt.tight_layout()
plt.show()
