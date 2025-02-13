#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Parameters for the Gaussian distributions
mu1 = 2  # Mean of the first Gaussian (blue)
mu2 = 3  # Mean of the second Gaussian (orange)
sigma = 1  # Standard deviation (same for both Gaussians)

# Points of interest
x0 = 2  # Green vertical line at x = 2 (center of first Gaussian)
x_prime = 3  # Red vertical line at x = 3 (center of second Gaussian)

# Generate data points for the Gaussians
x_values = np.linspace(0, 5, 1000)
y1_values = norm.pdf(x_values, mu1, sigma)  # First Gaussian (blue)
y2_values = norm.pdf(x_values, mu2, sigma)  # Second Gaussian (orange)

# Create the plot
plt.figure(figsize=(10, 6))

# Plot the Gaussian distributions
plt.plot(x_values, y1_values, label=f'Gaussian (μ={mu1}, σ={sigma})', color='blue')
plt.plot(x_values, y2_values, label=f'Gaussian (μ={mu2}, σ={sigma})', color='orange')

# Draw a green vertical line at x = 2 and label it as x_0
plt.axvline(x=x0, color='green', linestyle='-', linewidth=2, label=f'$x_0$ = {x0}')
plt.text(x0, -0.02, f'$x_0$ = {x0}', fontsize=12, color='green', ha='center', va='top')

# Draw a red vertical line at x = 3 and label it as x'
plt.axvline(x=x_prime, color='red', linestyle='-', linewidth=2, label=f"$x'$ = {x_prime}")
plt.text(x_prime, -0.02, f"$x'$ = {x_prime}", fontsize=12, color='red', ha='center', va='top')

# Find the intersection of the green vertical line (x0=2) with the ORANGE Gaussian (mu=3)
p_x0_orange = norm.pdf(x0, mu2, sigma)  # p(x) at x=2 for the orange Gaussian

# Draw a dashed horizontal line at this intersection
plt.axhline(y=p_x0_orange, color='black', linestyle='--', linewidth=1.5, alpha=0.7)
plt.text(x0 + 0.1, p_x0_orange + 0.01, f'p($x_0$) = {p_x0_orange:.3f}', fontsize=12, color='black')

# Add labels, title, and legend
plt.xlabel('x')
plt.ylabel('Probability Density')
plt.title('Using Gaussian as q(x) implies $q(x_0|x\') = q(x\'|x_0)$', fontsize=14)
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
