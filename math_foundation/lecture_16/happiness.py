#!/usr/bin/env python
import numpy as np
from numpy import array

# Define Q, c, and d
Q = array([[2,   1,   0.8],
           [1,   3,   0.6],
           [0.8, 0.6, 2.5]])
c = array([7, 5, 10])
d = 3

# Gradient of F(x): ߜF(x) = -Qx + c
def ߜF(f, r, s):
    ߜf = -2*f - r - 0.8*s + 7
    ߜr = -f - 3*r - 0.6*s + 5
    ߜs = -0.8*f - 0.6*r - 2.5*s + 10
    return [ߜf, ߜr, ߜs]


def optimize_fulfillment(f=1.0, r=1.0, s=1.0, step=0.0001):
    while True:
        [ߜf, ߜr, ߜs] = ߜF(f, r, s)

        # Update each variable in the direction of its gradient
		# note that sign(+) = 1 and sign(-) = -1
        f += step * np.sign(ߜf)
        r += step * np.sign(ߜr)
        s += step * np.sign(ߜs)

        #print('f = %.3f, r = %.3f, s = %.3f, ߜf = %.3f, ߜr = %.3f, ߜs = %.3f'%(f, r, s, ߜf, ߜr, ߜs))
        # Stop when all partials are non-positive
        if np.all(array([ߜf, ߜr, ߜs]) <= 0):
            break
    return [f, r, s]

# Run
optimal_f, optimal_r, optimal_s = optimize_fulfillment()

# Print results
print(f"Optimal f (friend time) = {optimal_f:.3f}")
print(f"Optimal r (reflection) = {optimal_r:.3f}")
print(f"Optimal s (school work) = {optimal_s:.3f}")

