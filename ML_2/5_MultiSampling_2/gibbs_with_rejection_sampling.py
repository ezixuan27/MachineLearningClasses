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

def conditional_gaussian(μ, Σ, xշ, n):
    μₐ = μ[0, 0]
    μᵦ = μ[1, 0]
    Σₐₐ = Σ[0, 0]
    Σᵦᵦ = Σ[1, 1]
    Σₐᵦ = Σ[0, 1]
    Σᵦᵦˉᣳ = 1 / Σᵦᵦ
    μₐӏᵦ = μₐ + Σₐᵦ * Σᵦᵦˉᣳ * (xշ - μᵦ)
    Σₐӏᵦ = Σₐₐ - Σₐᵦ * Σᵦᵦˉᣳ * Σₐᵦ
    σ = sqrt(Σₐӏᵦ)
    return np.random.normal(μₐӏᵦ, σ, n)

def gibbs_sampling(n):
    samples = np.zeros((n, 2))
    x₁, x₂ = 3, 2
    for i in range(n):
        x₁ = conditional_gaussian(μ, Σ, x₂, 1)[0]
        x₂ = conditional_gaussian(μ[::-1], Σ[::-1, ::-1], x₁, 1)[0]
        samples[i] = [x₁, x₂]
    return samples

def rejection_sampling(n):
    samples = []
    while len(samples) < n:
        x₁, x₂ = np.random.randn(2) * sqrt(np.diag(Σ)) + μ.flatten()
        ρ = Σ[0, 1] / (sqrt(Σ[0, 0]) * sqrt(Σ[1, 1]))
        target = ē(-0.5 * ((x₁ - μ[0, 0]) ** 2 / Σ[0, 0] + (x₂ - μ[1, 0]) ** 2 / Σ[1, 1] - 2 * ρ * (x₁ - μ[0, 0]) * (x₂ - μ[1, 0]) / (sqrt(Σ[0, 0]) * sqrt(Σ[1, 1]))))
        proposal = norm.pdf(x₁, μ[0, 0], sqrt(Σ[0, 0])) * norm.pdf(x₂, μ[1, 0], sqrt(Σ[1, 1]))
        if np.random.rand() < target / proposal:
            samples.append([x₁, x₂])
    return np.array(samples)

# Generate samples
n_samples = 9000
samples_gibbs = gibbs_sampling(n_samples)
samples_rejection = rejection_sampling(n_samples)

# Compute sample mean and covariance
μᵍ = np.mean(samples_gibbs, axis=0)
Σᵍ = np.cov(samples_gibbs, rowvar=False)
μʳ = np.mean(samples_rejection, axis=0)
Σʳ = np.cov(samples_rejection, rowvar=False)

# Plot results
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.scatter(samples_gibbs[:, 0], samples_gibbs[:, 1], alpha=0.3, s=2)
plt.title(f'Gibbs Sampling\nμ={μᵍ}, Σ={Σᵍ}')
plt.xlabel('x1')
plt.ylabel('x2')

plt.subplot(1, 2, 2)
plt.scatter(samples_rejection[:, 0], samples_rejection[:, 1], alpha=0.3, s=2)
plt.title(f'Rejection Sampling\nμ={μʳ}, Σ={Σʳ}')
plt.xlabel('x1')
plt.ylabel('x2')

plt.tight_layout()
plt.show()

