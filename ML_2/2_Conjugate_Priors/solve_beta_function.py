#!/usr/bin/env python

from scipy.integrate import quad
from scipy.special import beta as Ɓᴾʸ
from scipy.stats import beta as pᴾʸ

# Define the Beta function using numerical integration
def B(α, β):
	def f(t): return t**(α - 1) * (1 - t)**(β - 1)
	result, _ = quad(f, 0, 1)
	return result

# Compare the results
print("Your own Beta function: ", B(1, 2))
print("Python's Beta function: ", Ɓᴾʸ(1, 2))


def p(i, α, β):
	return (i**(α-1) * (1 - i)**(β-1)) / B(α,β)

# Compare the results
print("Your own Beta probability of i = 0.4: ", p(0.4, 2, 4))
print("Python's Beta probability of i = 0.4: ", pᴾʸ.pdf(0.4, 2, 4))

