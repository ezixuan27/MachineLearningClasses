#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
from mpl_toolkits.mplot3d import Axes3D

# Parameters
mean = [3, 2]  # Center of the Gaussian distribution (μ)
cov = [[1, 0], [0, 1]]  # Covariance matrix (isotropic)
x_prime = [4, 1]  # Point to mark as x'

# Create a grid of points
x, y = np.meshgrid(np.linspace(0, 6, 100), np.linspace(0, 4, 100))
pos = np.dstack((x, y))

# Compute the 2D Gaussian distribution
rv = multivariate_normal(mean, cov)
z = rv.pdf(pos)

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the Gaussian surface
ax.plot_surface(x, y, z, cmap='viridis', alpha=0.8)

# Draw a long green vertical line at μ (mean) and label it as x_0
line_height = 1.2 * np.max(z)  # Extend the line higher than the Gaussian surface
ax.plot([mean[0], mean[0]], [mean[1], mean[1]], [0, line_height], 
        color='g', linestyle='-', linewidth=3, label="$x_0$ = μ")
ax.text(mean[0], mean[1], line_height + 0.01, f"$x_0$ = {mean}", fontsize=12, color='green', ha='center')

# Draw a red vertical line at (4, 1) and label it as x'
ax.plot([x_prime[0], x_prime[0]], [x_prime[1], x_prime[1]], [0, line_height], 
        color='r', linestyle='--', linewidth=3, label="x'")
ax.text(x_prime[0], x_prime[1], line_height + 0.01, f"x' = {x_prime}", fontsize=12, color='red', ha='center')

# Mark the point (4, 1) on the surface
ax.scatter([x_prime[0]], [x_prime[1]], [rv.pdf(x_prime)], color='r', s=100)

# Add labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Probability Density')
ax.set_title('2D Isotropic Gaussian Distribution in 3D')

# Add a legend
ax.legend()

# Show the plot
plt.show()
