#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters
mu = 3  # Mean (center) of the Gaussian distribution
sigma = 1  # Standard deviation
x_prime = mu + sigma  # 1 standard deviation point

# Generate data points for the Gaussian distribution
x_values = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
y_values = norm.pdf(x_values, mu, sigma)

# Plot the Gaussian distribution
plt.plot(x_values, y_values, label=f'Gaussian (μ={mu}, σ={sigma})')

# Draw a vertical line at μ and label it as $x_0$
plt.axvline(x=mu, color='g', linestyle='-', label=f'$x_0$ = μ = {mu}')
plt.text(mu, norm.pdf(mu, mu, sigma) - 0.2, f'$x_0$ = {mu}', fontsize=12, color='green', ha='center')

# Draw a vertical line at x' (1 standard deviation)
plt.axvline(x=x_prime, color='r', linestyle='--', label=f"x' = {x_prime}")

# Mark the point x' on the plot
plt.scatter([x_prime], [norm.pdf(x_prime, mu, sigma)], color='red')
plt.text(x_prime, norm.pdf(x_prime, mu, sigma) + 0.02, f"x' = {x_prime}", fontsize=12, color='red', ha='center')

# Add labels and legend
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('μ = x_0, sampled x\' ')
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
