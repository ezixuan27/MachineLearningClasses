#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 0.05  # mean
sigma = 0.006  # standard deviation

# Create points for x-axis (cover ±4 standard deviations)
#x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
x = np.linspace(0, 1, 1000)

# Create Gaussian distribution
y = norm.pdf(x, mu, sigma)

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', lw=2, label=f'N(μ={mu}, σ={sigma})')

# Fill under the curve
plt.fill_between(x, y, alpha=0.3, color='blue')

# Add vertical line at mean
plt.axvline(x=mu, color='red', linestyle='--', label='Mean = 0.05')

# Add lines for standard deviation ranges
plt.axvline(x=mu+sigma, color='green', linestyle=':', label='±1σ')
plt.axvline(x=mu-sigma, color='green', linestyle=':')

# Customize the plot
plt.title(f'Gaussian Distribution (μ={mu}, σ={sigma})')
plt.xlabel('(i) Interest Level')
plt.ylabel('Probability Density')
plt.grid(True, alpha=0.3)
plt.legend()

# Set axis limits
plt.xlim(0, 1)
plt.ylim(0, max(y) * 1.1)

plt.savefig('gaussian.png')
plt.tight_layout()
plt.show()
