#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Symmetric matrix A (diagonalizable with real eigenvalues)
A = np.array([
    [3, 1],
    [1, 2]
])

# Eigen-decomposition: A = V Λ V^T
eigenvalues, V = np.linalg.eigh(A)  # 'eigh' guarantees orthonormal eigenvectors for symmetric A
Λ = np.diag(eigenvalues)

# Normalize eigenvectors (already orthonormal from eigh)
assert np.allclose(V @ V.T, np.eye(2)), "V is not orthonormal"

# Initial matrix B with multiple column vectors
B = np.array([
    [1, 1],
    [0, 1]
], dtype=float)

# Normalize columns of B
B = B / np.linalg.norm(B, axis=0)

# Dominant eigenvector (largest eigenvalue)
dominant_index = np.argmax(eigenvalues)
dominant_vec = V[:, dominant_index]

# Plot setup
fig, ax = plt.subplots()
iterations = [1, 2, 5, 10, 20, 50]

print('EigenVectors')
print(V, '\n\n\n')

for k in iterations:
    Λk = np.diag(eigenvalues**k)
    Ak = V @ Λk @ V.T
    AkB = Ak @ B

    # Normalize columns for direction
    AkB = AkB / np.linalg.norm(AkB, axis=0)

    print(k)
    print(AkB, '\n\n')
#    for col in AkB.T:
#        ax.quiver(0, 0, col[0], col[1], angles='xy', scale_units='xy', scale=1, alpha=0.5, label=f"A^{k}")

## Plot dominant eigenvector
#ax.quiver(0, 0, dominant_vec[0], dominant_vec[1], color='black', linewidth=2, scale=1,
#          scale_units='xy', label='dominant eigenvector')
#
#ax.set_xlim(-1.1, 1.1)
#ax.set_ylim(-1.1, 1.1)
#ax.set_aspect('equal')
#ax.grid(True)
#ax.set_title("Power Method via Eigendecomposition: $A^k B$ Alignment")
#ax.legend()
#plt.show()

