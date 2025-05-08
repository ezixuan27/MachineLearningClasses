#!/usr/bin/env python
import numpy as np
from numpy.linalg import eig, eigh, norm
np.set_printoptions(suppress=True, precision=4)


def pretty_np_array(m, title=None, end_space=''):
	m = str(m)
	L1 = m.split('\n')
	L1_max_width = len(max(L1, key=len))
	if title is not None:
		t1 = str.center(title, L1_max_width)
		m = t1 + '\n' + m + end_space
	else: m = m + end_space
	print(m, '\n')

# Original matrix A and eigenvalue matrix Λ
A = np.array([
    [2, -2, 0, 0],
    [-2, 2, 0, 0],
    [0, 0, 2.5005, -2.4995],
    [0, 0, -2.4995, 2.5005]
])

# Eigen-decomposition (A should already be symmetric)
λ, V = eigh(A)  # `eigh` guarantees real symmetric output and orthonormal V

# Verify A = V Λ Vᵀ
Λ = np.diag(λ)
Aᣳ = V @ Λ @ V.T
pretty_np_array(Aᣳ, title='Original Reconstruction A = V Λ Vᵀ')

# Step 2 - Remove trivial eigenvalue (0)
non_trivial_indices = np.where(λ > 1e-10)[0]
Λ̃ = np.diag(λ[non_trivial_indices])
Ṽ = V[:, non_trivial_indices]
Ã = Ṽ @ Λ̃ @ Ṽ.T
pretty_np_array(Ã, title='Non-trivial reconstruction : Ã = Ṽ Λ̃ Ṽᵀ')

# Step 3 - Remove trivial and *almost* trivial (e.g., eigenvalue < 0.01)
core_indices = np.where(λ > 0.01)[0]
Λ̄ = np.diag(λ[core_indices])
V̄ = V[:, core_indices]
Aᑦ = V̄ @ Λ̄ @ V̄.T
pretty_np_array(Aᑦ, title='Core Reconstruction')




