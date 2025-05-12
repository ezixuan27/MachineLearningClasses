#!/usr/bin/env python



n = 100
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
np.savetxt('imputation_small.csv', B, delimiter=',', fmt='%.5f')
#import pdb; pdb.set_trace()


