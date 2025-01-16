#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

# Parameters for the Beta distribution
alpha = 1  # Shape parameter 1
beta_param = 19  # Shape parameter 2
mean = alpha / (alpha + beta_param)  # Mean of the Beta distribution

# Generate x values from 0 to 1
x = np.linspace(0, 1, 1000)

# Compute the PDF of the Beta distribution
pdf = beta.pdf(x, alpha, beta_param)

# Plot the Beta distribution
plt.figure(figsize=(8, 6))
plt.plot(x, pdf, label=f"Beta(α={alpha}, β={beta_param})", color="blue")

# Add a vertical line at the mean value
plt.axvline(mean, color="red", linestyle="--", label=f"Mean = {mean:.2f}")

# Add title, labels, and legend
plt.title(f"Beta Distribution (Mean = {mean:.2f})", fontsize=16)
plt.xlabel("(i) Interest Level", fontsize=14)
plt.ylabel("Probability Density", fontsize=14)
plt.xlim(0, 1)  # Set x-axis range from 0 to 1
plt.ylim(0, max(pdf) + 1)  # Adjust y-axis range for better visualization
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend(fontsize=12)

plt.savefig('beta.png')
plt.tight_layout()
plt.show()
