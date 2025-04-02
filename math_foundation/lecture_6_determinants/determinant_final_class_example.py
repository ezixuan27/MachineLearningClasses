#!/usr/bin/env python

import numpy as np
from numpy.linalg import inv, det

# Define the matrix D
D = np.array([
    [2, 3, 1, 0, 0, 0, 0],
    [1, 2, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 0, 0],
    [0, 0, 0, 3, 2, 0, 0],
    [0, 0, 0, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 1]
])


Dˉᣳ = inv(D)
ӏDˉᣳӏ = det(2*Dˉᣳ)
print(f"The determinant of 2 * (D^-1) is: {ӏDˉᣳӏ}")
