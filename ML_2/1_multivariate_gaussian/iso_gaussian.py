#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

Ձπ = 2*np.pi

# Custom Isotropic Gaussian Function
def isotropic_gaussian(x, μ, σ):
	x = np.array(x).reshape((2,1))
	d = μ.shape[0]  # Dimensionality
	normalization = (Ձπ * σ**2) ** (d / 2)  # Normalization constant
	return (np.exp(-0.5 * (x - μ).T.dot(x - μ) / σ**2) / normalization).item()


# Define the mean and standard deviations
μ = np.array([[1], [1]])
σ_values = [2, 0.2]

# Create a grid for plotting
x = np.linspace(-3, 5, 100)
y = np.linspace(-3, 5, 100)
x, y = np.meshgrid(x, y)

# Create a heatmap plot for each σ value
plt.figure(figsize=(12, 6))

for i, σ in enumerate(σ_values):
	# Initialize z as an empty array
	z = np.zeros_like(x)
	
	# Compute z through a loop
	for row in range(x.shape[0]):
		for col in range(x.shape[1]):
			# Evaluate the custom isotropic Gaussian function at each point
			point = np.array([x[row, col], y[row, col]])
			z[row, col] = isotropic_gaussian(point, μ, σ)
	
	# Create a subplot
	plt.subplot(1, 2, i+1)
	
	# Plot the heatmap
	heatmap = plt.contourf(x, y, z, levels=50, cmap='viridis')
	
	# Add labels and title
	plt.title(f'Isotropic Gaussian ($σ = %.3f$)'%σ)
	plt.xlabel('$x_1$')
	plt.ylabel('$x_2$')
	
	# Add a color bar
	plt.colorbar(heatmap, label='Probability Density')

plt.tight_layout()
plt.show()
