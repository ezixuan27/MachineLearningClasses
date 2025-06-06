#!/usr/bin/env python
import numpy as np
from space import space, point_cloud

class InteractiveDemo(space):
    def __init__(self):
        super().__init__()  # Properly initialize the space window

        # Original object matrix P
        self.P = np.array([
            [3, 1, 2],
            [5, 1, 2],
            [5, 4, 2],
            [3, 4, 2],
            [3, 1, 5],
            [5, 1, 5],
            [5, 4, 5],
            [3, 4, 5]
        ])

        # Compute the mean
        self.center = self.P.mean(axis=0)

        # Draw object
        self.pc = point_cloud(self.P, color=(0.3, 0.6, 1.0, 1))

        # Current scaling factor
        self.scale = 1.0

        # Accept key presses
        self.accept("x", self.rotate_x)
        self.accept("y", self.rotate_y)
        self.accept("z", self.rotate_z)
        self.accept("s", self.scale_down)
        self.accept("b", self.scale_up)

    def center_transform_restore(self, matrix):
        X = self.pc.pos() - self.center
        X = X @ matrix.T
        X = X + self.center
        self.pc.redraw(X)

    def rotate_x(self):
        θ = np.radians(10)
        Rx = np.array([
            [1, 0, 0],
            [0, np.cos(θ), -np.sin(θ)],
            [0, np.sin(θ),  np.cos(θ)]
        ])
        self.center_transform_restore(Rx)

    def rotate_y(self):
        θ = np.radians(10)
        Ry = np.array([
            [np.cos(θ), 0, np.sin(θ)],
            [0, 1, 0],
            [-np.sin(θ), 0, np.cos(θ)]
        ])
        self.center_transform_restore(Ry)

    def rotate_z(self):
        θ = np.radians(10)
        Rz = np.array([
            [np.cos(θ), -np.sin(θ), 0],
            [np.sin(θ),  np.cos(θ), 0],
            [0, 0, 1]
        ])
        self.center_transform_restore(Rz)

    def scale_up(self):
        self.scale = 1.1
        #self.scale *= 1.1

        S = np.eye(3) * self.scale
        self.center_transform_restore(S)

    def scale_down(self):
        self.scale = 0.9
        #self.scale /= 1.1
        S = np.eye(3) * self.scale
        self.center_transform_restore(S)

# Create and run the app
app = InteractiveDemo()
app.run()

