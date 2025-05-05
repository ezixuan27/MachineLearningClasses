#!/usr/bin/env python

import numpy as np
from numpy.linalg import norm, eig, matrix_power, inv
np.set_printoptions(precision=4, suppress=True)

# Define a symmetric (and thus diagonalizable) 3×3 matrix
A = np.array([
    [2, 0, 0],
    [0, 3, 1],
    [0, 1, 3]
], dtype=float)


B = np.array([
    [4, 0],
    [3, 0],
    [0, 5]
], dtype=float)


# Eigendecomposition: A = VΛVˉᣳ
λ, V = eig(A)
Λ = np.diag(λ)
Vˉᣳ = inv(V)  # inverse of V
v = V[:,0].reshape(-1,1) # the dominant eigenvector

# Power to raise A
n = 100 

# Naive method: repeated matrix power
A_naive = matrix_power(A, n)

# Diagonalization trick: Aⁿ = VΛⁿVˉᣳ
Λⁿ = np.diag(λ**n)
Aᣳᵒᵒ = V @ Λⁿ @ Vˉᣳ

# Output comparison
print("Naive Aⁿ:\n", A_naive)
print("\nSmart Aⁿ using VΛⁿVˉᣳ:\n", Aᣳᵒᵒ)

# --------------------
C = Aᣳᵒᵒ @ B
C = C/norm(C, axis=0)
print('\nThe dominant eigenvector of the msg\n',v)
print('\nYour mind after 100 exposures\n',C)
