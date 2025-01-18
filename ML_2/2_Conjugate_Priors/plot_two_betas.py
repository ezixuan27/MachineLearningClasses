#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma as Γ
from scipy.integrate import quad

# Define the Beta function
def B(α, β):
    return Γ(α) * Γ(β) / Γ(α + β)


# probability p(ĩ) for β distribution
def pᵝ(ĩ, α, β):
    return (ĩ ** (α - 1) * (1 - ĩ) ** (β - 1)) / B(α, β)


# Generate ĩ values
ĩ = np.linspace(0, 1, 1000)


# Parameters for the two Beta distributions
α1, β1 = 2, 19
α2, β2 = 1, 20

# Calculate the PDF values
y1 = pᵝ(ĩ, α1, β1)
y2 = pᵝ(ĩ, α2, β2)

# Calculate the probability of the Beta distribution being higher than 0.1
prob1, _ = quad(pᵝ, 0.1, 1, args=(α1, β1))
prob2, _ = quad(pᵝ, 0.1, 1, args=(α2, β2))



# Plot the Beta distributions
plt.figure(figsize=(12, 6))

# Plot for α = 2, β = 19
plt.subplot(1, 2, 1)
plt.plot(ĩ, y1, label=f'Beta(α={α1}, β={β1})', color='blue')
plt.fill_between(ĩ[ĩ >= 0.1], y1[ĩ >= 0.1], color='blue', alpha=0.3, label=f'P(X > 0.1) = {prob1:.4f}')
plt.title(f'Beta Distribution (α={α1}, β={β1})')
plt.xlabel('(ĩ) Interest Level')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)



# Plot for α = 1, β = 20
plt.subplot(1, 2, 2)
plt.plot(ĩ, y2, label=f'Beta(α={α2}, β={β2})', color='red')
plt.fill_between(ĩ[ĩ >= 0.1], y2[ĩ >= 0.1], color='red', alpha=0.3, label=f'P(X > 0.1) = {prob2:.4f}')
plt.title(f'Beta Distribution (α={α2}, β={β2})')
plt.xlabel('(ĩ) Interest Level')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
