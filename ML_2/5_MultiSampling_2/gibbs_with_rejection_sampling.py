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


#	 proposal distribution
def kq(xᵢ):
	k = 1
	return k*norm.pdf(xᵢ, 3, 1.5)

#	sampling distribution
def p(xₗ):
	k = 2
	d = 2
	#	if pass in a list of values
	if type(xₗ).__name__ == 'ndarray': 
		L = []
		for xᵢ in xₗ:
			ԶπᒄᐟᒾӏΣӏᣳᐟᒾ = sqrt(Զπ**d) * sqrt(np.linalg.det(Σ))
			Δ = np.array([[xᵢ.item()],[xշ]]) - μ
			L.append((1/(ԶπᒄᐟᒾӏΣӏᣳᐟᒾ)*ē(-0.5*Δ.T @ Σˉᣳ @  Δ)).item())
		return np.array(L)
	#	if pass in a single value
	else:
		ԶπᒄᐟᒾӏΣӏᣳᐟᒾ = sqrt(Զπ**d) * sqrt(np.linalg.det(Σ))
		Δ = np.array([[xₗ],[xշ]]) - μ
		return 1/(ԶπᒄᐟᒾӏΣӏᣳᐟᒾ)*ē(0.5*Δ.T @ Σˉᣳ @  Δ)

def rejection_sampling():
	n = 35000
	r = np.random.rand(n)
	v = 1.5*np.random.randn(n) + 3
	u = r*kq(v)
	pᵛ = p(v)
#
	samples = v[u < pᵛ] 
	μᵣ = np.mean(samples)
	σᵣ = np.std(samples)
#	
	return μᵣ, σᵣ, samples








# Generate samples
n_samples = 9000
samples_rejection = rejection_sampling(n_samples)

# Compute sample mean and covariance
μʳ = np.mean(samples_rejection, axis=0)
Σʳ = np.cov(samples_rejection, rowvar=False)

print(μʳ)
print(Σʳ)

# Plot results
plt.figure(figsize=(6, 5))
plt.scatter(samples_rejection[:, 0], samples_rejection[:, 1], alpha=0.3, s=2)
plt.title(f'Gibbs with Rejection Sampling')
plt.xlabel('x1')
plt.ylabel('x2')

plt.tight_layout()
plt.show()

