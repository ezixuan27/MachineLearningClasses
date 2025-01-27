#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# Parameters
μ = 0.5  # Mean of the exponential distribution
sample_size = 4000  # Number of samples

# Generate samples from the exponential distribution
samples = np.random.exponential(scale=μ, size=sample_size)

# Create a histogram of the samples
plt.hist(samples, bins=50, density=True, color='blue', alpha=0.7, label='Histogram')

# Overlay the theoretical exponential distribution
x = np.linspace(0, max(samples), 1000)
pdf = expon.pdf(x, scale=μ)  # Probability density function
plt.plot(x, pdf, 'r-', lw=2, label='Exponential PDF')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Density')
plt.title('Exponential Distribution (μ=0.5)')
plt.legend()

# Use tight_layout to adjust spacing
plt.tight_layout()

# Show the plot
plt.show()
