#!/usr/bin/env python
import numpy as np
from space import space
from panda3d.core import LineSegs, NodePath, Vec3

def project_vector_onto_plane(x, basis):
    V = np.vstack([v.T for v in basis])  # Stack as rows
    VVt_inv = np.linalg.inv(V @ V.T)
    return (V.T @ VVt_inv @ V @ x).flatten()

def create_dashed_line(render, start, end, color=(0.5, 0.5, 0.5, 1), dash=0.1, gap=0.1):
    segs = LineSegs()
    segs.setColor(*color)
    segs.setThickness(2)

    start = Vec3(*start)
    end = Vec3(*end)
    direction = end - start
    total = direction.length()
    direction.normalize()

    d = 0.0
    while d < total:
        a = start + direction * d
        d += dash
        b = start + direction * min(d, total)
        segs.moveTo(a)
        segs.drawTo(b)
        d += gap

    NodePath(segs.create()).reparentTo(render)

class App(space):
    def __init__(self):
        super().__init__()

        # Hardcoded rotated orthogonal vectors (rotated 20° in xy plane)
        e1 = np.array([[ 0.9397], [ 0.3420], [0]])
        e2 = np.array([[-0.3420], [ 0.9397], [0]])

        # 3D vector to project
        x = np.array([[1], [1], [1]])

        # Draw basis
        self.v1 = self.create_vector(e1.flatten(), color=(1, 0, 0, 1))   # red
        self.v2 = self.create_vector(e2.flatten(), color=(0, 1, 0, 1))   # green

        # Original vector
        self.v3 = self.create_vector(x.flatten(), color=(0, 0, 1, 1))    # blue

        # Project x onto plane
        x_proj = project_vector_onto_plane(x, [e1, e2])
        self.v_proj = self.create_vector(x_proj, color=(0.5, 0.5, 0.5, 1))  # gray

        # Connect projection
        create_dashed_line(self.render, x_proj, x.flatten())

if __name__ == "__main__":
    App().run()

