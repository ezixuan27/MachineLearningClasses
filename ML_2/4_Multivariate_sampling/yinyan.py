#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Parameters
grid_size = 500  # Number of grid points in each dimension
x_range = (-2, 2)  # Range of x values
y_range = (-2, 2)  # Range of y values
mu_r = 1.0  # Mean radius of the ring
sigma_r = 0.2  # Standard deviation of the Gaussian for the ring
mu_dot = 0.3  # Radius of the small dots
sigma_dot = 0.1  # Standard deviation of the Gaussian for the dots
k = 10  # Sigmoid steepness parameter

# Create a grid of points in 2D space
x = np.linspace(x_range[0], x_range[1], grid_size)
y = np.linspace(y_range[0], y_range[1], grid_size)
X, Y = np.meshgrid(x, y)

# Convert Cartesian coordinates (x, y) to polar coordinates (r, theta)
R = np.sqrt(X**2 + Y**2)  # Radius
Theta = np.arctan2(Y, X)  # Angle

# Define the sigmoid function
def sigmoid(x, k):
    return 1 / (1 + np.exp(-k * x))

# Define the Yin and Yang halves
p_yin = np.exp(-0.5 * ((R - mu_r) / sigma_r)**2) * sigmoid(Theta - np.pi, k)
p_yang = np.exp(-0.5 * ((R - mu_r) / sigma_r)**2) * sigmoid(-Theta, k)

# Define the Yin and Yang dots
p_yin_dot = np.exp(-0.5 * ((R - mu_dot) / sigma_dot)**2) * sigmoid(Theta, k)
p_yang_dot = np.exp(-0.5 * ((R - mu_dot) / sigma_dot)**2) * sigmoid(Theta - np.pi, k)

# Combine all components
pdf = p_yin + p_yang + p_yin_dot + p_yang_dot

# Normalize the PDF (optional, for visualization)
pdf /= np.max(pdf)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
surf = ax.plot_surface(X, Y, pdf, cmap='viridis', alpha=0.8)

# Add color bar
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=10, label="Probability Density")

# Set labels
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('3D Yin-Yang Distribution')

# Show plot
plt.show()
