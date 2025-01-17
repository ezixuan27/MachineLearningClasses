#!/usr/bin/env python

import numpy as np
from numpy import array
from numpy import trace

v = array([[1],[2],[3]])
print(v)


u = array([[3],[1],[4]])
print(u)


A = array([[1,2,3],[3,2,1],[3,1,1]])
print(A)


# outer product $u v^{\top}$
print(u.dot(v.T))


# inner/dot product $v^{\top} v$
print(v.T.dot(v))


# $x^{\top} A x$
print(v.T.dot(A).dot(v))


# hadamard
print(v*u)


# matrix inner product
print(trace(A.dot(A.T)))


