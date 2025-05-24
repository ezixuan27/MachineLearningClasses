#!/usr/bin/env python

# ### Problem: Maximize Happiness
# We want to maximize:
# $$ -\frac{1}{2}x^\top Q x + c^\top x + d, \quad \text{where} \quad Q = \begin{bmatrix} 2 & 1 & 0 \\ 1 & 2 & 0 \\ 0 & 0 & 1 \end{bmatrix}, \quad c = \begin{bmatrix} 5 \\ 4 \\ 3 \end{bmatrix} $$

import numpy as np
from scipy.optimize import minimize

# Define Q and c
Q = np.array([[2, 1, 0],
              [1, 2, 0],
              [0, 0, 1]])
c = np.array([5, 4, 3])

# Define the objective function (negative because we want to maximize)
def f(x):
    return 0.5 * x @ Q @ x - c @ x

# Initial guess
x0 = np.zeros(3)

# Solve
result = minimize(f, x0)

# Output
print("Optimal x:", result.x)
print("Maximum value:", -result.fun)

