#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt

# Step 1: Define 4 points in 2D
X = np.array([
	[2, 3],
	[4, 7],
	[5, 1],
	[6, 4]
], dtype=float)

# Step 2: Number of points
n = X.shape[0]

# Step 3: Build the centering matrix C = I - (1/n) * 11ᵀ
I = np.eye(n)
one_matrix = np.ones((n, n))
C = I - (1/n) * one_matrix

# Step 4: Apply centering
X_centered = C @ X

# Step 5: Plot before and after
plt.figure(figsize=(10, 5))

def plot_dots(img_id, label, X):
	plt.subplot(1, 2, img_id)
	plt.scatter(X[:, 0], X[:, 1], color='blue', s=80, label=label)

	"""Helper to draw x and y axes"""
	plt.axhline(0, color='black', linewidth=1.2)
	plt.axvline(0, color='black', linewidth=1.2)
	plt.xlim(-8, 8)
	plt.ylim(-8, 8)
	plt.grid(True, linestyle='--', linewidth=0.7)

	plt.title(label)
	plt.xlabel("x")
	plt.ylabel("y")
	plt.legend()

plot_dots1, "Original Points", X)
plot_dots1, "Centered Points", X_centered)

plt.tight_layout()
plt.show()

