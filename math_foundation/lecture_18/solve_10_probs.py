#!/usr/bin/env python
import numpy as np
from scipy.optimize import minimize

# Problem 1
def f1(x):  # $$ f(x) = x^2 - 4x + 3 $$
    return x[0]**2 - 4*x[0] + 3
result = minimize(f1, [0])
print("1:", result.x)

# Problem 2
def f2(x):  # $$ f(x) = 2x^2 - 8x + 5 $$
    return 2*x[0]**2 - 8*x[0] + 5
result = minimize(f2, [0])
print("2:", result.x)

# Problem 3
def f3(v):  # $$ f(x, y) = x^2 + y^2 - 6x - 4y + 13 $$
    x, y = v
    return x**2 + y**2 - 6*x - 4*y + 13
result = minimize(f3, [0, 0])
print("3:", result.x)

# Problem 4
def f4(v):  # $$ f(x, y) = (x-2)^2 + (y+1)^2 $$
    x, y = v
    return (x - 2)**2 + (y + 1)**2
result = minimize(f4, [0, 0])
print("4:", result.x)

# Problem 5
Q5 = np.array([[2, 0], [0, 2]])
c5 = np.array([4, 6])
def f5(x):  # $$ f(x) = x^T Q x - c^T x $$
    return x @ Q5 @ x - c5 @ x
result = minimize(f5, [0, 0])
print("5:", result.x)

# Problem 6
Q6 = np.array([[1, 1], [1, 2]])
c6 = np.array([1, 1])
def f6(x):  # $$ f(x) = \frac{1}{2} x^T Q x - c^T x $$
    return 0.5 * x @ Q6 @ x - c6 @ x
result = minimize(f6, [0, 0])
print("6:", result.x)

# Problem 7
A7 = np.array([[3, 0], [0, 1]])
b7 = np.array([6, 2])
def f7(x):  # $$ f(x) = x^T A x - b^T x $$
    return x @ A7 @ x - b7 @ x
result = minimize(f7, [0, 0])
print("7:", result.x)

# Problem 8
c8 = np.array([5, -3])
def f8(x):  # $$ f(x) = ||x - c||^2 $$
    return np.sum((x - c8)**2)
result = minimize(f8, [0, 0])
print("8:", result.x)

# Problem 9
one = np.array([1, 1])
def f9(x):  # $$ f(x) = (x - 1)^T (x - 1) $$
    return np.sum((x - one)**2)
result = minimize(f9, [0, 0])
print("9:", result.x)

# Problem 10
def f10(v):  # $$ f(x, y, z) = x^2 + y^2 + z^2 - 2x - 4y + 6z $$
    x, y, z = v
    return x**2 + y**2 + z**2 - 2*x - 4*y + 6*z
result = minimize(f10, [0, 0, 0])
print("10:", result.x)

