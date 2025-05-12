#!/usr/bin/env python

import numpy as np
from numpy.linalg import eigh
from numpy import genfromtxt

A = genfromtxt('imputation_missing_10.csv', delimiter=',')
#A = genfromtxt('imputation.csv', delimiter=',')
print('A[0,0] original was 0.0736')
A[0, 0] = 0 # setting unknow value to 0

# Step 5: Eigendecomposition
[Ū, σ̄ , V̄ᵀ] = np.linalg.svd(A)  

# I already printed out the singular values 
# and identified that the first 4 eigenvectors are core
k = 4  
idx = np.argsort(np.abs(σ̄))[::-1]
σ̄ = σ̄[idx[:k]]		# truncate the singular values
Ū = Ū[:, idx[:k]]	# truncate the U 
V̄ᵀ = V̄ᵀ[idx[:k], :] # truncate the V

# Step 7: Reconstruct B_lowrank = V Σ V^T
Σ̄  = np.diag(σ̄)
Ā = Ū  @ Σ̄ @ V̄ᵀ

# Step 8: Print reconstructed A[0,0]
print("Reconstructed A[0,0]:", Ā[0, 0])




