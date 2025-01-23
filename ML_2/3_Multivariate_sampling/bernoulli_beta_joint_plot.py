#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta as beta_function
from mpl_toolkits.mplot3d import Axes3D

# Parameters for the Beta distribution
alpha_1 = 2.0
beta_1 = 5.0

# Define the Beta distribution PDF
def beta_pdf(i, alpha, beta):
    return (i ** (alpha - 1)) * ((1 - i) ** (beta - 1)) / beta_function(alpha, beta)

# Define the Bernoulli distribution PMF
def bernoulli_pmf(t, i):
    return (i ** t) * ((1 - i) ** (1 - t))

# Define the joint distribution PDF
def joint_pdf(i, t, alpha, beta):
    return bernoulli_pmf(t, i) * beta_pdf(i, alpha, beta)

# Create a grid of i values (from 0 to 1) and t values (0 and 1)
i_values = np.linspace(0, 1, 100)
t_values = np.array([0, 1])

# Create a meshgrid for i and t
I, T = np.meshgrid(i_values, t_values)

# Evaluate the joint PDF over the grid
Z = joint_pdf(I, T, alpha_1, beta_1)

# Create 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot the surface
ax.plot_surface(I, T, Z, cmap='viridis', alpha=0.8)

# Set labels
ax.set_xlabel('i (Beta)')
ax.set_ylabel('t (Bernoulli)')
ax.set_zlabel('Joint Probability Density')
ax.set_title(f'Joint Distribution of Bernoulli and Beta (α={alpha_1}, β={beta_1})')

# Show the plot
plt.tight_layout()
plt.show()
