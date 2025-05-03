#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Symmetric matrix
A = np.array([
    [3, 1],
    [1, 2]
])

# Eigendecomposition
λ, V = np.linalg.eigh(A)
Λ = np.diag(λ)
Vᵀ = V.T
assert np.allclose(V @ Vᵀ, np.eye(2))

# Input matrix B
B = np.array([
    [1, 1],
    [0, 1]
], dtype=float)
B = B / np.linalg.norm(B, axis=0)

# Dominant eigenvector
dominant_index = np.argmax(λ)
d = V[:, dominant_index]
d = d / np.linalg.norm(d)

# Perpendicular unit vector
n = np.array([-d[1], d[0]])

# Margin width
ε = 0.1
offset1 = n * ε
offset2 = -n * ε

# Generate dashed lines
t = np.linspace(-1.5, 1.5, 100)
line1 = (d[:, np.newaxis] * t) + offset1[:, np.newaxis]
line2 = (d[:, np.newaxis] * t) + offset2[:, np.newaxis]

# Compute rotation angle for labels
θ_deg = np.degrees(np.arctan2(d[1], d[0]))
if θ_deg > 90 or θ_deg < -90:
    θ_deg += 180  # flip upside-down text

# Plot setup
iterations = [0, 1, 2, 5, 10, 20]
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
axes = [ax1, ax2]
titles = ["Column 1 of B", "Column 2 of B"]
colors = ['green'] + ['gray'] * (len(iterations) - 2) + ['red']

for i, col_idx in enumerate([0, 1]):
    ax = axes[i]
    b = B[:, col_idx]

    for j, k in enumerate(iterations):
        Λᵏ = np.diag(λ**k)
        Aᵏ = V @ Λᵏ @ Vᵀ
        v = Aᵏ @ b
        v = v / np.linalg.norm(v)
        ax.quiver(0, 0, v[0], v[1], angles='xy', scale_units='xy', scale=1, color=colors[j])

        if k == 0:
            ax.text(v[0]*1.1, v[1]*1.1, "start", color='black', fontsize=10)
        elif k == 20:
            ax.text(v[0]*1.1, v[1]*1.1, "end", color='black', fontsize=10)

    # Dominant eigenvector
    ax.quiver(0, 0, d[0], d[1], angles='xy', scale_units='xy', scale=1,
              color='blue', linestyle='dashed')

    # Label: dominant eigenvector (2-line label)
    label_pos = d * 1.1
    ax.text(label_pos[0], label_pos[1], "dominant\neigenvector",
            color='black', fontsize=10, ha='center', va='center', rotation=θ_deg)

    # Dashed blue lines
    ax.plot(line1[0], line1[1], linestyle='dashed', color='blue', linewidth=1)
    ax.plot(line2[0], line2[1], linestyle='dashed', color='blue', linewidth=1)

    # Center and outside positions
    center_pos = d * 0.7
    outside1 = center_pos + n * (ε + 0.05)
    outside2 = center_pos - n * (ε + 0.05)

    # Inside label = Illusion
    ax.text(center_pos[0], center_pos[1], "Illusion", color='black',
            fontsize=11, ha='center', va='center', rotation=θ_deg)

    # Outside label = Reality
    ax.text(outside1[0], outside1[1], "Reality", color='black',
            fontsize=11, ha='center', va='center', rotation=θ_deg)
    ax.text(outside2[0], outside2[1], "Reality", color='black',
            fontsize=11, ha='center', va='center', rotation=θ_deg)

    ax.set_xlim(-1.2, 1.2)
    ax.set_ylim(-1.2, 1.2)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.set_title(titles[i])

plt.tight_layout()
plt.show()

