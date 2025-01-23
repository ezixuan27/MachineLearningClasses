#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from mpl_toolkits.mplot3d import Axes3D

# Parameters
alpha = 1
beta_param = 19

# Generate i values and compute Beta PDF
i = np.linspace(0, 0.3, 1000)
beta_pdf = beta.pdf(i, alpha, beta_param)

# Joint distributions for t=0 and t=1
joint_t0 = (1 - i) * beta_pdf  # p(t=0, i)
joint_t1 = i * beta_pdf        # p(t=1, i)

# Create 3D plot
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')

# Plot t=0 and t=1 as separate lines in 3D space
ax.plot(i, np.zeros_like(i), joint_t0, label='$t=0$', color='blue', lw=2)
ax.plot(i, np.ones_like(i), joint_t1, label='$t=1$', color='red', lw=2)

# Axis labels and styling
ax.set_xlabel('$i$', fontsize=12)
ax.set_ylabel('$t$', fontsize=12)
ax.set_zlabel('Joint Density $p(t, i)$', fontsize=12)
ax.set_title('3D Joint Distribution: Bernoulli + Beta(1, 19)', fontsize=14, pad=20)
ax.set_yticks([0, 1])  # Discrete t values
ax.view_init(elev=20, azim=-45)  # Adjust viewing angle
ax.legend()

plt.tight_layout()
plt.show()
