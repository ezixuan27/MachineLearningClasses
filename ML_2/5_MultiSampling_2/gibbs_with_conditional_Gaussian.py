#!/usr/bin/env python

import numpy as np
from numpy import exp as ē
from numpy import sqrt
from numpy.linalg import inv
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy.stats import norm

# Set random seed
np.random.seed(42)
Զπ = 2*np.pi

# Parameters
μ = np.array([[3], [2]])
Σ = np.array([[1, 1], [1, 2]])
Σˉᣳ = inv(Σ)

def conditional_gaussian(μ, Σ, xշ):
    μₐ = μ[0, 0]
    μᵦ = μ[1, 0]
    Σₐₐ = Σ[0, 0]
    Σᵦᵦ = Σ[1, 1]
    Σₐᵦ = Σᵦₐ = Σ[0, 1]
    Σᵦᵦˉᣳ = 1 / Σᵦᵦ
    μₐӏᵦ = μₐ + Σₐᵦ * Σᵦᵦˉᣳ * (xշ - μᵦ)
    Σₐӏᵦ = Σₐₐ - Σₐᵦ * Σᵦᵦˉᣳ * Σᵦₐ
    σ = sqrt(Σₐӏᵦ)
    return np.random.normal(μₐӏᵦ, σ)

def gibbs_sampling(n):
    samples = np.zeros((n, 2))
    xₗ, xշ = 3, 2
    for i in range(n):
        xₗ = conditional_gaussian(μ, Σ, xշ)
        xշ = conditional_gaussian(μ[::-1], Σ[::-1, ::-1], xₗ)
        samples[i] = [xₗ, xշ]
    return samples

# Generate samples
n_samples = 20000
samples_gibbs = gibbs_sampling(n_samples)


# Compute sample mean and covariance
μᵍ = np.mean(samples_gibbs, axis=0)
Σᵍ = np.cov(samples_gibbs, rowvar=False)
print(μᵍ)
print(Σᵍ)

# Plot results
plt.figure(figsize=(6, 5))
plt.scatter(samples_gibbs[:, 0], samples_gibbs[:, 1], alpha=0.3, s=2)
plt.title("Gibbs Sampling")
plt.xlabel("x1")
plt.ylabel("x2")
plt.tight_layout()
plt.show()


