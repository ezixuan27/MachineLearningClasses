#!/usr/bin/env python

import autograd.numpy as np
from autograd import grad

y = np.array([[2], [5]])
ӏ = np.array([[1], [1]])
x = np.random.random((2, 1))
w = np.array([[7], [8]])

#	Problem 1
def f(x,y,ӏ):
    return np.dot(np.transpose(y), x) + np.dot(np.transpose(x), ӏ)

grad_foo = grad(f)

print("Autograd: \n", grad_foo(x,y,ӏ))
print("Theoretical: \n", np.array([[3], [6]]))





#	Problem 2
A = np.array([	[2, 1], 
				[1, 1]])
def f(x, A):
    return np.dot(np.dot(np.transpose(x), A), x)

def ߜf(x, A):
	return 2*A.dot(x)


grad_foo = grad(f)

print("Autograd: \n", grad_foo(x, A))
print("Theoretical: \n", ߜf(x, A))



#	Problem 3
A = np.array([	[4, 0], 
				[1, 1]])
def f(x, A):
    return np.exp(np.dot(np.dot(np.transpose(x), A), x))

def ߜf(x, A):
	v = (A + np.transpose(A)).dot(x)
	return f(x,A)*v


grad_foo = grad(f)
print("Autograd: \n", grad_foo(x, A))
print("Theoretical: \n", ߜf(x, A))




#	Problem 4
A = np.array([	[4, 0], 
				[1, 1]])
def eˉᵂˣ(w,x):
	return np.exp(np.dot(np.transpose(w), x))

def f(x, w):
    return np.linalg.inv(1 + eˉᵂˣ(w,x))

def ߜf(x, w):
	return (eˉᵂˣ(w,x)/(1 + eˉᵂˣ(w,x))**2)*w

grad_foo = grad(f)
print("Autograd: \n", grad_foo(x, w))
print("Theoretical: \n", ߜf(x, w))




