#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import multivariate_normal

# Given mean vector and covariance matrix
μ = np.array([[70, 100, 5, 8]]).T
Σ = np.array([	[25, 15, 2, -4],
                [15, 64, 12, -3],
                [2, 12, 9, -1],
                [-4, -3, -1, 1]])

x̂ = np.array([[66, 85, 8, 8]]).T  # Grandmother's observed values

# Extract relevant blocks for conditional distribution p(x2, x3 | x1, x4)
μₐ = μ[1:3]  # Mean of x2, x3
μᵦ = μ[[0, 3]]  # Mean of x1, x4

Σₐₐ = Σ[1:3, 1:3]  # Covariance of x2, x3
Σᵦᵦ = Σ[[0, 3]][:, [0, 3]]  # Covariance of x1, x4
Σₐᵦ = Σ[1:3, [0, 3]]  # Covariance of (x2, x3) with (x1, x4)

# Compute conditional mean and covariance for p(x2, x3 | x1, x4)
Σᵦᵦˉᣳ = np.linalg.inv(Σᵦᵦ)

μₐӏᵦ = μₐ + Σₐᵦ @ Σᵦᵦˉᣳ @ (x̂[[0, 3]] - μᵦ)
Σₐӏᵦ = Σₐₐ - Σₐᵦ @ Σᵦᵦˉᣳ @ Σₐᵦ.T
import pdb; pdb.set_trace()

# Create a grid for plotting
x2_vals = np.linspace(μₐӏᵦ[0] - 23, μₐӏᵦ[0] + 23, 50)
x3_vals = np.linspace(μₐӏᵦ[1] - 23, μₐӏᵦ[1] + 23, 50)
X2, X3 = np.meshgrid(x2_vals, x3_vals)
pos = np.dstack((X2, X3))

# Compute the probability density function
rv = multivariate_normal(μₐӏᵦ, Σₐӏᵦ)
Z = rv.pdf(pos)

# Print conditional mean and covariance
print(μₐӏᵦ, Σₐӏᵦ)

# 3D Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X2, X3, Z, cmap='viridis', alpha=0.7)

# Plot grandmother's location
grandmother_pdf_value = rv.pdf([x̂[1], x̂[2]])
ax.scatter(x̂[1], x̂[2], grandmother_pdf_value, color='red', s=100, label="Grandmother location")

ax.set_xlabel("Fasting Glucose Level (x2) [mg/dL]")
ax.set_ylabel("CRP Level (x3) [mg/L]")
ax.set_zlabel("Probability Density")
ax.set_title("Conditional Distribution p(x2, x3 | x1, x4)")
ax.legend()

plt.show()


