#!/usr/bin/env python

# We want to minimize the function:
# $$ f(\mathbf{x}) = \mathbf{x}^\top A \mathbf{x} - \mathbf{b}^\top \mathbf{x} $$

import numpy as np
from scipy.optimize import minimize

# Define matrix A and vector b
A = np.array([[2, 1],
              [1, 3]])
b = np.array([4, 5])

# Define the objective function
def f(x):
    return x @ A @ x - b @ x

# Initial guess
x0 = np.array([0.0, 0.0])

# Minimize
result = minimize(f, x0)

# Output
print("Optimal x:", result.x)
print("Minimum value:", result.fun)

