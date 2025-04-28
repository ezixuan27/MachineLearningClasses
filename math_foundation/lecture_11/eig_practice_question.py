#!/usr/bin/env python
import numpy as np
from numpy import diag
from numpy.linalg import eig, inv
from scipy.linalg import null_space

# Define the matrix A
A = np.array([[-6, 3],
              [4, 5]])

# Eigenvalues and eigenvectors 
[λ,V] = eig(A)
print(λ)
print(V)

# Null Space
print(null_space(V.T))


# Diagonalization
Σ = diag(λ)
Vˉᣳ = inv(V)
print(V @ Σ @ Vˉᣳ)

# Not symmetric
print(V @ Σ @ V.T)



