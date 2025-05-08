#!/usr/bin/env python

import numpy as np
from numpy.linalg import eigh

n = 1000
# Step 1: Create a low-rank matrix A
A = np.random.randn(n,n)  # A will be 3000x3000 but rank 10
[U,σ,Vᵀ] = np.linalg.svd(A)  # eigh because B is symmetric
Σ = np.zeros((n,n))
Σ[0,0] = 100
Σ[1,1] = 99
Σ[2,2] = 9
Σ[3,3] = 0.3
Σ[4,4] = 0.01


# Step 2: Symmetrize A to get B
B = U @ Σ @ Vᵀ

# Step 3: Print B[0,0]
print("Original B[0,0]:", B[0, 0])

# Step 4: Set B[0,0] to 0
B[0, 0] = 0 #np.mean(B)
print("Set to mean B[0,0]:", B[0, 0])

# Step 5: Eigendecomposition
[Ū, σ̄ , V̄ᵀ] = np.linalg.svd(B)  # eigh because B is symmetric

# Step 6: Truncate small eigenvalues
# Keep top k largest magnitude eigenvalues
k = 4  # we know rank ~10, so this is natural
idx = np.argsort(np.abs(σ̄))[::-1]
σ̄ = σ̄[idx[:k]]
Ū = Ū[:, idx[:k]]
V̄ᵀ = V̄ᵀ[idx[:k], :]

# Step 7: Reconstruct B_lowrank = V Σ V^T
Σ̄  = np.diag(σ̄)
B̄ = Ū  @ Σ̄ @ V̄ᵀ

# Step 8: Print reconstructed B[0,0]
print("Reconstructed B[0,0]:", B̄[0, 0])

# (Optional) Check reconstruction error
error = np.linalg.norm(B - B̄) / np.linalg.norm(B)
print("Relative Reconstruction Error:", error)
