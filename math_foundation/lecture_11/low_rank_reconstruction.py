#!/usr/bin/env python

import numpy as np
from numpy.linalg import eigh


# Step 1: Create a low-rank matrix A
A = np.random.randn(3000,3000)  # A will be 3000x3000 but rank 10
λ, V = np.linalg.eigh(A)  # eigh because B is symmetric
Λ = np.zeros((3000,3000))
Λ[0,0] = 100
Λ[1,1] = 99
Λ[2,2] = 9
Λ[3,3] = 0.3
Λ[4,4] = 0.14


# Step 2: Symmetrize A to get B
B = V @ Λ @ V.T

# Step 3: Print B[0,0]
print("Original B[0,0]:", B[0, 0])

# Step 4: Set B[0,0] to 0
B[0, 0] = np.mean(B)
print("Set to mean B[0,0]:", B[0, 0])

# Step 5: Eigendecomposition
eigvals, eigvecs = np.linalg.eigh(B)  # eigh because B is symmetric

# Step 6: Truncate small eigenvalues
# Keep top k largest magnitude eigenvalues
k = 4  # we know rank ~10, so this is natural
idx = np.argsort(np.abs(eigvals))[::-1]
eigvals_truncated = eigvals[idx[:k]]
eigvecs_truncated = eigvecs[:, idx[:k]]

# Step 7: Reconstruct B_lowrank = V Σ V^T
Sigma_truncated = np.diag(eigvals_truncated)
B_reconstructed = eigvecs_truncated @ Sigma_truncated @ eigvecs_truncated.T

# Step 8: Print reconstructed B[0,0]
print("Reconstructed B[0,0]:", B_reconstructed[0, 0])

# (Optional) Check reconstruction error
error = np.linalg.norm(B - B_reconstructed) / np.linalg.norm(B)
print("Relative Reconstruction Error:", error)
import pdb; pdb.set_trace()
