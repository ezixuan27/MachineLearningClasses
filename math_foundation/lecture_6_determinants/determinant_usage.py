#!/usr/bin/env python

import numpy as np

# Command to find determinant
A = np.array([	[3,2,1],
				[1,1,1],
				[1,2,1]])

d = np.linalg.det(A)
print(d)
