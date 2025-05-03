#!/usr/bin/env python

import numpy as np

# Define a symmetric (and thus diagonalizable) 3×3 matrix
A = np.array([
    [4, 1, 1],
    [1, 3, 0],
    [1, 0, 2]
], dtype=float)

# Eigendecomposition: A = VΛVˉᣳ
λ, V = np.linalg.eig(A)
Λ = np.diag(λ)
Vˉᣳ = np.linalg.inv(V)  # inverse of V

# Power to raise A
n = 3

# Naive method: repeated matrix power
A_naive = np.linalg.matrix_power(A, n)

# Diagonalization trick: Aⁿ = VΛⁿVˉᣳ
Λⁿ = np.diag(λ**n)
A_smart = V @ Λⁿ @ Vˉᣳ

# Output comparison
print("Naive Aⁿ:\n", A_naive)
print("\nSmart Aⁿ using VΛⁿVˉᣳ:\n", A_smart)

