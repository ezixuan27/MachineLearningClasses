#!/usr/bin/env python

import numpy as np
from sklearn.preprocessing import PolynomialFeatures

X = np.array([	[1,0],
				[2,1],
				[0,1]])

#[1, a, b, a^2, ab, b^2].
poly = PolynomialFeatures(2)
newX = poly.fit_transform(X)
print(newX)

