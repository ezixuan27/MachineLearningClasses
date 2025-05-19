#!/usr/bin/env python
from scipy.integrate import quad

# Problem 1: ∫₁² 3x² dx
def f1(x):
    return 3 * x**2

A1, _ = quad(f1, 1, 2)

# Problem 2: ∫₀⁴ (4x³ - 2x² + x) dx
def f2(x):
    return 4 * x**3 - 2 * x**2 + x

A2, _ = quad(f2, 0, 4)

# Problem 3: ∫₂⁵ 7 dx
def f3(x):
    return 7

A3, _ = quad(f3, 2, 5)

# Problem 4: ∫₀¹ (x² + 1)(x³) dx → expanded as x⁵ + x³
def f4(x):
    return x**5 + x**3

A4, _ = quad(f4, 0, 1)

# Print results
print("Problem 1: Area = %.4f" % A1)
print("Problem 2: Area = %.4f" % A2)
print("Problem 3: Area = %.4f" % A3)
print("Problem 4: Area = %.4f" % A4)

