#!/usr/bin/env python

import numpy as np

# Original full matrix
M = np.array([
    [5, 3, 2, 1],
    [4, 2, 3, 1],
    [1, 1, 4, 5],
    [2, 2, 5, 4]
], dtype=float)

# Create the corrupted version with the missing entry
M_missing = M.copy()
M_missing[1, 2] = np.mean(M)  # Replace the (2,3) entry (index 1,2) with zero (or np.nan if you handle it differently)

# Perform SVD
U, Σ, Vᵀ = np.linalg.svd(M_missing, full_matrices=False)

# Keep only top 3 singular values
Σշ = np.diag(Σ[:3])
Uշ = U[:, :3]
Vᵀշ = Vᵀ[:3, :]

# Reconstruct rank-2 approximation
M_approx = Uշ @ Σշ @ Vᵀշ

# Predicted value at position (2,3)
predicted = M_approx[1, 2]
actual = M[1, 2]

print("Predicted value at (2,3):", predicted)
print("Actual value at (2,3):", actual)
print("Absolute error:", abs(predicted - actual))

