#!/usr/bin/env python
import numpy as np

# A and y from the displayed augmented matrix
A = np.array([
    [1,   1/2,  -1/2,  3/2,   1],
    [0,     1,     1,   -1,  6/5],
    [0,     0,     1, -5/8,  1/8],
    [0,     0,     0,    1, 13/15],
    [0,     0,     0,    0,  1/3],
], dtype=float)

y = np.array([
    7/2,
    -11/5,
    -11/8,
    17/15,
    -1/3,
], dtype=float)

# Given solution vector
x = np.array([1, 1, 0, 2, -1], dtype=float)

Ax = A @ x

print("A @ x =", Ax)
print("y     =", y)
print("A @ x equals y? ", np.allclose(Ax, y))

