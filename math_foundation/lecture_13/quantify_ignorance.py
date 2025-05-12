#!/usr/bin/env python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('imputation.csv', header=None).values.astype(float)

# Settings
n_loops = 9
errors = []
rank_fraction = 0.2  # keep top 20% singular values (can adjust)

# Loop from 10% to 90%
for i in range(1, n_loops + 1):
    missing_fraction = i * 0.1
    corrupted_data = data.copy()

    # Generate mask of missing entries
    mask = np.random.rand(*data.shape) < missing_fraction
    corrupted_data[mask] = 0
   
    # SVD on corrupted data
    U, Σ, Vᵀ = np.linalg.svd(corrupted_data, full_matrices=False)

    # Keep only top k singular values (low-rank approximation)
    k = 5
    Σ_low = np.diag(Σ[:k])
    U_low = U[:, :k]
    Vᵀ_low = Vᵀ[:k, :]

    # Reconstruct
    reconstructed = U_low @ Σ_low @ Vᵀ_low

    # Calculate Frobenius norm error only on the corrupted entries
    error = np.linalg.norm((reconstructed - data) * mask, 'fro') / np.linalg.norm(data * mask, 'fro')

    errors.append(error)

    print(f"Removed {int(missing_fraction * 100)}% of data - Low-rank ({k}) Relative Error (Frobenius norm): {error:.4f}")

# Plot the error curve
plt.figure()
plt.plot(np.arange(10, 100, 10), errors, marker='o')
plt.title('Ignorance Score vs. Missing Entry Percentage')
plt.xlabel('Percentage of Data Set to Zero (%)')
plt.ylabel('Ignorance Score')
plt.grid(True)
plt.show()

