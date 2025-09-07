#!/usr/bin/env python
import numpy as np


for i in range(100):
	# Step 1: Generate two random 3x3 matrices
	rand_A = np.random.randn(3, 3)
	rand_B = np.random.randn(3, 3)
	
	# Step 2: Use QR decomposition to get orthonormal matrices A and B
	A, _ = np.linalg.qr(rand_A)
	B, _ = np.linalg.qr(rand_B)
	
	# Step 3: Multiply Aᵀ * B
	print(np.sum(A.T @ A), np.sum(A.T @ B))
	if np.sum(A.T @ A) < np.sum(A.T @ B):
		print('\n\n')

