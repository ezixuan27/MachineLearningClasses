#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from numpy.linalg import norm, eig

# Matrix A
A = np.array([[2, 1],
              [1, 2]])

# Find eigenvectors
eigenvalues, eigenvectors = eig(A)
dominant_index = np.argmax(np.abs(eigenvalues))
u_eigen = eigenvectors[:, dominant_index]
u_eigen = u_eigen / norm(u_eigen)

# Starting vector
u = np.array([-1, 2])
u = u / norm(u)

# Set up the plot
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True)

# Plot eigenvector once
eigen_line, = ax.plot([0, u_eigen[0]], [0, u_eigen[1]], color='red', label='Eigenvector')

# Starting vector (will be updated)
vector_line, = ax.plot([0, u[0]], [0, u[1]], color='green', label='Vector')

# Title and legend
ax.set_title("Vector converging to Eigenvector")
ax.legend()

# Frames of vectors
vectors = [u.copy()]
for _ in range(20):
    u = A.dot(u)
    u = u / norm(u)
    vectors.append(u.copy())

# Animation function
def animate(i):
    vec = vectors[i]
    vector_line.set_data([0, vec[0]], [0, vec[1]])
    return vector_line,

# Create animation
ani = animation.FuncAnimation(fig, animate, frames=len(vectors), interval=200, blit=True)

# Save to gif
ani.save('vector_to_eigenvector.gif', writer='pillow', fps=1)

print("GIF saved as vector_to_eigenvector.gif")

