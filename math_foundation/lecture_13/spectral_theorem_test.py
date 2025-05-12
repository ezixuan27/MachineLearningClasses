#!/usr/bin/env python
import numpy as np

# Define the matrix
A = np.array([
    [4, 2],
    [2, 3]
], dtype=float)

# Eigendecomposition
λ, V = np.linalg.eigh(A)  # Since A is symmetric, use eigh

# Sort eigenvalues and eigenvectors from largest to smallest for clarity
idx = np.argsort(λ)[::-1]
λ = λ[idx]
V = V[:, idx]

print("Eigenvalues:", λ)
print("Eigenvectors (columns):\n", V)

# Full reconstruction
v1 = V[:, 0].reshape(-1,1)	# extract eigv 1
v2 = V[:, 1].reshape(-1,1)	# extract eigv 2
A_full = λ[0] * v1 @ v1.T + λ[1] * v2 @ v2.T
print("\nFull reconstruction A:")
print(np.round(A_full, 4))

# Low-rank reconstruction (setting λ2 = 0)
A_low_rank = λ[0] * v1 @ v1.T
print("\nLow-rank reconstruction A (λ2 = 0):")
print(np.round(A_low_rank, 4))

# Difference
print("\nDifference between original A and low-rank reconstruction:")
print(np.round(A - A_low_rank, 4))

