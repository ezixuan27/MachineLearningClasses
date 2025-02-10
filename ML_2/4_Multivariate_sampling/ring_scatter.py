#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
n_samples = 1000  # Number of samples
radius = 2        # Radius of the ring
noise_std = 0.1   # Standard deviation of noise

# Generate angles uniformly distributed around the circle
theta = np.random.uniform(0, 2 * np.pi, n_samples)

# Generate radii with some noise
r = radius + np.random.normal(0, noise_std, n_samples)

# Convert polar coordinates (r, theta) to Cartesian coordinates (x, y)
x = r * np.cos(theta)
y = r * np.sin(theta)

# Add a third dimension (z) with some noise
z = np.random.normal(0, noise_std, n_samples)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Scatter plot
ax.scatter(x, y, z, s=10, alpha=0.6, c=theta, cmap='hsv')

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('3D Ring-Shaped Distribution')

# Show plot
plt.show()
