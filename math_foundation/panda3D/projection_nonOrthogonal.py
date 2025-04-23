#!/usr/bin/env python

import numpy as np
from space import space, tuple_vector_to_numpy

def project_vector_onto_plane(vec, basis_vectors):
    V = np.vstack([v.T for v in basis_vectors])  # Stack as rows
    VVt_inv = np.linalg.inv(V @ V.T)
    projection = V.T @ VVt_inv @ V @ vec
    return projection.flatten()

class App(space):
    def __init__(self):
        super().__init__()

        # Adjusted non-orthogonal vectors in x-y plane
        v1 = np.array([[1], [0.5], [0]])   # Skewed vector 1
        v2 = np.array([[0.2], [1], [0]])   # Skewed vector 2

        # Draw the 2D basis vectors
        self.v1_obj = self.create_vector((1, 0.5, 0), color=(1, 0, 0, 1))   # Red
        self.v2_obj = self.create_vector((0.2, 1, 0), color=(0, 1, 0, 1))   # Green

        # Define and draw the 3D vector
        v3 = np.array([[1], [1], [1]])
        self.v3_obj = self.create_vector(v3.flatten(), color=(0, 0, 1, 1))   # Blue

        # Project v3 onto the plane spanned by v1 and v2
        proj = project_vector_onto_plane(v3, [v1, v2])
        self.proj_obj = self.create_vector(proj, color=(0.5, 0.5, 0.5, 1))   # Gray projection

        # Also draw a connecting dashed line (optional) from tip of projection to tip of v3
        self.create_vector(proj, start=(1,1,1), color=(0.5, 0.5, 0.5, 0.6), thickness=2)

if __name__ == "__main__":
    app = App()
    app.run()

