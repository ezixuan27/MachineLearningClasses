#!/usr/bin/env python
import numpy as np

# Coefficient matrix A
A = np.array([
    [2,  1, -1,  3,  2],
    [1,  3,  2, -1,  4],
    [3, -1,  4,  2,  1],
    [2,  2,  1,  1,  3],
    [1, -1,  3,  2,  2]
], dtype=float)


# Right-hand side vector b
b = np.array([7, -2, 5, 3, 2], dtype=float)

# Solve Ax = b using NumPy
x = np.linalg.solve(A, b)

# Print solution
#x = np.array([[1],[1],[0],[2],[-1]]) # actual solution
print("Solution vector x:")
print(x)

# Verify the solution
print("\nCheck A @ x:")
print(A @ x)
print("Should equal b:")
print(b)

