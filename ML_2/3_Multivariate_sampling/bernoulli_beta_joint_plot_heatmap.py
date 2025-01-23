#!/usr/bin/env python

import matplotlib as mpl
mpl.rcParams['savefig.directory'] = '/home/chieh/code/MachineLearningClasses/ML_2/3_Multivariate_sampling'

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import beta as beta_function

# Parameters for the Beta distribution
alpha_1 = 1.0
beta_1 = 19.0

# Define the Beta distribution PDF
def beta_pdf(i, alpha, beta):
    return (i ** (alpha - 1)) * ((1 - i) ** (beta - 1)) / beta_function(alpha, beta)

# Define the Bernoulli distribution PMF
def bernoulli_pmf(t, i):
    return (i ** t) * ((1 - i) ** (1 - t))

# Define the joint distribution PDF
def joint_pdf(i, t, alpha, beta):
    return bernoulli_pmf(t, i) * beta_pdf(i, alpha, beta)

# Create a grid of i values (from 0 to 1)
i_values = np.linspace(0, 0.1, 100)

# Evaluate the joint PDF for t = 0 and t = 1
Z0 = joint_pdf(i_values, 0, alpha_1, beta_1)  # t = 0
Z1 = joint_pdf(i_values, 1, alpha_1, beta_1)  # t = 1

# Combine the results into a 2D array for the heatmap
Z = np.vstack([Z1, Z0])  # t = 1 on top, t = 0 at the bottom

# Plot the heatmap
plt.figure(figsize=(10, 4))

# Use extent to center t = 0 and t = 1 in their respective regions
plt.imshow(Z, extent=[0, 1, 0.25, 1.75], aspect='auto', cmap='viridis', origin='upper')

# Add color bar
cbar = plt.colorbar()
cbar.set_label('Joint Probability Density')

# Set labels
plt.xlabel('i (Beta)')
plt.ylabel('t (Bernoulli)')

# Set y-axis ticks to 0.5 and 1.5 (middle of the regions for t = 0 and t = 1)
plt.yticks([0.5, 1.5], ['0', '1'])

# Add title
plt.title(f'Joint Distribution of Bernoulli and Beta (α={alpha_1}, β={beta_1})')

# Show the plot
plt.show()
