#!/usr/bin/env python
"""
Projection & rotated‑axis demo
— longer basis lines, smaller teapot, AND labels x′ y′ z′ on the new axes.
Built on Chieh’s space.py.
"""

import math
import numpy as np
from panda3d.core import Vec3, Mat3, Mat4
from space import space                       # your helper module

# ---------- helpers --------------------------------------------------------

def rot_matrix_z(theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[c, -s, 0],
                     [s,  c, 0],
                     [0,  0, 1]])

def rot_matrix_y(theta):
    c, s = math.cos(theta), math.sin(theta)
    return np.array([[ c, 0, s],
                     [ 0, 1, 0],
                     [-s, 0, c]])

def np_to_vec3(v):
    return Vec3(float(v[0]), float(v[1]), float(v[2]))

def mat3_from_columns(x, y, z):
    """Build a Panda3D Mat3 whose COLUMNS are x, y, z (all Vec3)."""
    return Mat3(x[0], y[0], z[0],
                x[1], y[1], z[1],
                x[2], y[2], z[2])

# ---------- main app -------------------------------------------------------

class ProjectionDemo(space):
    def __init__(self):
        super().__init__()                     # grid, axes, camera, controls

        # --------------------------------------------------------------
        # 1.  Rotated orthonormal basis  R = R_y(30°)  ·  R_z(45°)
        # --------------------------------------------------------------
        R = rot_matrix_y(math.radians(30)) @ rot_matrix_z(math.radians(45))

        axis_len = 5.0                         # make rotated axes long
        ex, ey, ez = R[:, 0] * axis_len, \
                     R[:, 1] * axis_len, \
                     R[:, 2] * axis_len

        # Draw rotated axes (yellow, magenta, cyan)
        self.vx = self.create_vector(ex, color=(1, 1, 0, 1), thickness=5)
        self.vy = self.create_vector(ey, color=(1, 0, 1, 1), thickness=5)
        self.vz = self.create_vector(ez, color=(0, 1, 1, 1), thickness=5)

        # --------------------------------------------------------------
        # 2.  Labels at 110 % of each tip
        # --------------------------------------------------------------
        self._label_rot_axis("x", ex, (1, 1, 0, 1))
        self._label_rot_axis("y", ey, (1, 0, 1, 1))
        self._label_rot_axis("z", ez, (0, 1, 1, 1))

        # --------------------------------------------------------------
        # 3.  Node for the rotated frame
        # --------------------------------------------------------------
        self.basis_np = self.render.attachNewNode("rotated_basis")

        m3 = mat3_from_columns(np_to_vec3(R[:, 0]),
                               np_to_vec3(R[:, 1]),
                               np_to_vec3(R[:, 2]))
        self.basis_np.setMat(Mat4(m3))         # promote to 4×4

        # --------------------------------------------------------------
        # 4.  Load the teapot under the rotated node
        # --------------------------------------------------------------
        self.teapot = self.loader.loadModel("models/teapot")
        self.teapot.reparentTo(self.basis_np)
        self.teapot.setScale(0.4)              # smaller teapot

        # --------------------------------------------------------------
        # 5.  Spin the teapot about its local x′ axis
        # --------------------------------------------------------------
        self.taskMgr.add(self.spin_teapot, "SpinTeapot")

    # ---------- helpers ----------------------------------------------------

    def _label_rot_axis(self, text, vec_np, color):
        """Place a TextNode 10 % beyond the tip of vec_np."""
        tip = 1.1 * vec_np                     # 110 % for separation
        self.create_axis_label(text,
                               float(tip[0]), float(tip[1]), float(tip[2]),
                               color)

    # ---------- task: spin --------------------------------------------------

    def spin_teapot(self, task):
        self.teapot.setP((task.time * 45) % 360)   # 45 °/s pitch
        return task.cont

# ---------- run it ---------------------------------------------------------

if __name__ == "__main__":
    ProjectionDemo().run()

