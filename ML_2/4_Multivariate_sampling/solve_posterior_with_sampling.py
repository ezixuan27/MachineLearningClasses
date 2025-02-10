#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta  # Only needed for theoretical PDF


# Parameters
α_prior = 1
β_prior = 19
n = 10000

# Generate samples using numpy.random
np.random.seed(42)
i_samples = np.random.beta(α_prior, β_prior, n)  # Beta samples
t_samples = np.random.binomial(n=1, p=i_samples)  # Bernoulli samples (0/1)

# Split samples based on texting outcome
i_given_t1 = i_samples[t_samples == 1]
i_given_t0 = i_samples[t_samples == 0]

# Create figure with two subplots
plt.figure(figsize=(12, 5))

# Function to plot histograms with overlaid distributions
def plot_distribution(data, ax, title, condition):
    # Plot histogram
    ax.hist(data, bins=50, density=True, color='blue', alpha=0.7, label='Samples')
    
    # Calculate theoretical distribution
    x = np.linspace(0, 1, 1000)
    if condition == 1:
        # Posterior parameters when t=1: Beta(α+1, β)
        pdf = beta.pdf(x, α_prior + 1, β_prior)
    else:
        # Posterior parameters when t=0: Beta(α, β+1)
        pdf = beta.pdf(x, α_prior, β_prior + 1)
    
    # Plot theoretical distribution
    ax.plot(x, pdf, 'r-', lw=2, label='Theoretical PDF')
    ax.set_title(title)
    ax.set_xlabel('Interest Level (i)')
    ax.set_ylabel('Density')
    ax.legend()

# Plot for t=1
ax1 = plt.subplot(1, 2, 1)
plot_distribution(i_given_t1, ax1, r'$p(i \mid t=1)$', condition=1)

# Plot for t=0
ax2 = plt.subplot(1, 2, 2)
plot_distribution(i_given_t0, ax2, r'$p(i \mid t=0)$', condition=0)

plt.tight_layout()
plt.show()

# Calculate probabilities p(0.1 < i | t=1)
p_0ᐧ1ㄑi_t1 = np.sum(i_given_t1 > 0.1) / i_given_t1.size
p_0ᐧ1ㄑi_t0 = np.sum(i_given_t0 > 0.1) / i_given_t0.size

print(f"Probability of interest > 10% given they texted back: {p_0ᐧ1ㄑi_t1:.4f}")
print(f"Probability of interest > 10% given they didn't text back: {p_0ᐧ1ㄑi_t0:.4f}")
