#!/usr/bin/env python

import autograd.numpy as np
from autograd import grad
from autograd.numpy import exp, log2, log


# Problem 1
def f1(x):
    return 1.0 * x + 2.0 * x + 3.0 * x

df1 = grad(f1)
print("Problem 1 manual derivative:", 6)
print("Problem 1 autograd derivative at x=2:", df1(2.0))


# Problem 2
def f2(x):
    return (2.0 * x + 1.0)**2 + 3.0 * x - 2.0

df2 = grad(f2)
print("\nProblem 2 manual derivative at x=1:", 8*1 + 7)
print("Problem 2 autograd derivative at x=1:", df2(1.0))


# Problem 3
def f3(x):
    return (2.0 * x + 1.0) * exp(-2.0 * x) - log2(x**2)

def manual3(x):
	return 2*exp(-2*x) - 2 * (2*x + 1)*exp(-2*x) - 2/(x * log(2))

df3 = grad(f3)
print("\nProblem 3 manual derivative at x=1:", manual3(1.0))
print("Problem 3 autograd derivative at x=1.0:", df3(1.0))


# Problem 4
def f4(x):
    return (exp(2.0 * x) + 1.0)**3 + log(x**2)

def manual4(x):
	return 6*exp(2*x)*(exp(2*x) + 1)**2 + 2/x

df4 = grad(f4)
print("\nProblem 4 manual derivative at x=1:", manual4(1.0))
print("Problem 4 autograd derivative at x=1.0:", df4(1.0))


# Problem 5
def f5(x):
    return np.sqrt(x**2 + 1.0)

df5 = grad(f5)
print("\nProblem 5 manual derivative at x=1.0:", 1.0 / np.sqrt(2.0))
print("Problem 5 autograd derivative at x=1.0:", df5(1.0))


# Problem 6
def f6(x):
    return (3.0 * x**2 + 5.0) * exp(-x)

def manual6(x):
	return (-3*x**2 + 6*x -5) * exp(-x)

df6 = grad(f6)
print("\nProblem 6 manual derivative at x=1:", manual6(1.0))
print("Problem 6 autograd derivative at x=1.0:", df6(1.0))


# Problem 7
def f7(x):
    return log(np.sqrt(1.0 + x**2))

def manual7(x):
	return x/(1+x**2)


df7 = grad(f7)
print("\nProblem 7 manual derivative at x=1:", manual7(1.0))
print("Problem 7 autograd derivative at x=1.0:", df7(1.0))


# Problem 8 (using product rule style)
def f8(x):
    return (x**3 + 2.0 * x) * (x**2 + 1.0)**-1

def manual8(x):
	return (3*x**2 + 2)/(x**2 + 1) - (2*x*(x**3 + 2*x))/(x**2 + 1)**2

df8 = grad(f8)
print("\nProblem 8 manual derivative at x=1:", manual8(1.0))
print("Problem 8 autograd derivative at x=1.0:", df8(1.0))


# Problem 9
def f9(x):
    return x**2 + 3.0 * x

df9 = grad(f9)
print("\nProblem 9 manual derivative at x=2.0:", 2.0 * 2.0 + 3.0)
print("Problem 9 autograd derivative at x=2.0:", df9(2.0))


# Problem 10
def f10(x):
    return exp(-2.0 * x)

df10 = grad(f10)
print("\nProblem 10 manual derivative at x=0.0:", -2.0)
print("Problem 10 autograd derivative at x=0.0:", df10(0.0))


# Problem 11
def f11(x):
    return log(x**2 + 1.0)

df11 = grad(f11)
print("\nProblem 11 manual derivative at x=1.0:", 2.0 / (1.0 + 1.0))
print("Problem 11 autograd derivative at x=1.0:", df11(1.0))

