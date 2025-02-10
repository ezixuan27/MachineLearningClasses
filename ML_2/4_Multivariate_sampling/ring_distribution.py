#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
radius = 4.0          # Radius of the ring
sigma = 1.4           # Standard deviation of the Gaussian around the ring
grid_size = 100       # Number of grid points in each dimension
x_range = (-10, 10)     # Range of x values
y_range = (-10, 10)     # Range of y values

# Create a grid of points in 2D space
x = np.linspace(x_range[0], x_range[1], grid_size)
y = np.linspace(y_range[0], y_range[1], grid_size)
X, Y = np.meshgrid(x, y)

# Convert Cartesian coordinates (x, y) to polar coordinates (r, theta)
R = np.sqrt(X**2 + Y**2)  # Radius
Theta = np.arctan2(Y, X)  # Angle

# Define the probability density function (PDF)
# Gaussian centered at the ring radius in the radial direction
pdf = np.exp(-0.5 * ((R - radius) / sigma)**2)

# Normalize the PDF (optional, for visualization)
pdf /= np.max(pdf)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the PDF as a 3D surface
ax.plot_surface(X, Y, pdf, cmap='viridis', alpha=0.8)

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('2D Ring-Shaped Distribution (PDF) in 3D')

# Show plot
plt.tight_layout()
plt.show()
