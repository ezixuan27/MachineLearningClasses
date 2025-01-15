#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import expon

# For exponential distribution, rate parameter λ = 1/mean
rate = 1/0.05  # lambda = 20 since mean = 0.05

# Create points for x-axis (up to 5 times the mean should cover most of the distribution)
x = np.linspace(0, 0.6, 1000)

# Create exponential distribution
y = rate * np.exp(-rate * x)  # PDF: λe^(-λx)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'r-', lw=2, label=f'Exponential(λ={rate:.2f})')

# Fill under the curve
plt.fill_between(x, y, alpha=0.3, color='red')

# Add vertical line at mean
plt.axvline(x=0.05, color='black', linestyle='--', label='Mean = 0.05')

# Customize the plot
plt.title(f'Exponential Distribution (mean = 0.05)')
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.legend()

# Set reasonable axis limits
plt.xlim(0, 1)
plt.ylim(0, max(y) * 1.1)

plt.tight_layout()
plt.show()
