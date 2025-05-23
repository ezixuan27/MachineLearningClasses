#!/usr/bin/env python

# We want to minimize the function:
# $$ f(x) = (x - 3)^2 + 1 $$

from scipy.optimize import minimize

# Define the univariate objective function
def f(x):
    return (x - 3)**2 + 1

# Initial guess
x0 = 0

# Minimize
result = minimize(f, x0)

# Output
print("Optimal x:", result.x[0])
print("Minimum value:", result.fun)

