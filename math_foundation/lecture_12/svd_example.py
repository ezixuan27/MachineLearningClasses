#!/usr/bin/env python

import numpy as np

# Define a 3×2 matrix
A = np.array([[1, 2],
              [3, 4],
              [5, 6]])

# Compute SVD
U, S, Vᵀ = np.linalg.svd(A)

# Construct Σ (3×2) from S
Σ = np.zeros((3, 2))
Σ[:2, :2] = np.diag(S)

# Reconstruct A
A_reconstructed = U @ Σ @ Vᵀ

# Display results
print("Original A:\n", A)
print("U:\n", U)
print("S (vector of singular values):\n", S)
print("Vᵀ:\n", Vᵀ)
print("Σ:\n", Σ)
print("Reconstructed A:\n", A_reconstructed)

