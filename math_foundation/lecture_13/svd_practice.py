#!/usr/bin/env python

import numpy as np
from numpy.linalg import svd
np.set_printoptions(suppress=True, precision=4)


def pretty_np_array(m, title=None, end_space=''):
	m = str(m)
	L1 = m.split('\n')
	L1_max_width = len(max(L1, key=len))
	if title is not None:
		t1 = str.center(title, L1_max_width)
		m = t1 + '\n' + m + end_space
	else: m = m + end_space
	print(m, '\n')


A = np.array([
    [3, 2, 2],
    [2, 3, -2]
])

[U,σ,Vᵀ] = svd(A) 
Σ = np.diag(σ)
Ꮙᵀ = Vᵀ[0:2, :] # Keeping only Core eigenvectors

pretty_np_array(U, title='U')
pretty_np_array(Σ, title='Σ')
pretty_np_array(Vᵀ, title='Vᵀ')
pretty_np_array(Ꮙᵀ, title='Ꮙᵀ')
pretty_np_array(U @ Σ @ Ꮙᵀ, title='Reconstruction UΣᏉᵀ')
