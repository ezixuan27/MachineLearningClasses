#!/usr/bin/env python
import numpy as np

# Define matrix X
X = np.array([
	[4.50, -3.50, 0.00],
	[-3.50, 4.50, 0.00],
	[0.00,  0.00, 2.00]
])

# Define matrix B
B = np.array([
	[1.00, 0.00,  0.00],
	[0.00, 3.00, -1.00],
	[0.00, -1.00, 3.00]
])

C = B
for i in range(2000):
	C = X @ C
	C = C/np.linalg.norm(C)

# Compute eigenvalues and eigenvectors of X
λ_X, V_X = np.linalg.eig(X)

# Compute eigenvalues and eigenvectors of C
λ_C, V_C = np.linalg.eig(C)

# Print results
np.set_printoptions(precision=4, suppress=True)

print("Eigenvalues of X:")
print(λ_X)
print("\nEigenvectors of X (columns of V_X):")
print(V_X)

print("\nEigenvalues of C = X^1000 @ B:")
print(λ_C)
print("\nEigenvectors of C (columns of V_C):")
print(V_C)

