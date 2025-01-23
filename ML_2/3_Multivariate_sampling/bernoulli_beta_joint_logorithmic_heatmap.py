#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from matplotlib.colors import LogNorm

# Parameters
alpha = 1
beta_param = 19
epsilon = 1e-10  # Small value to avoid log(0)

# Generate i values and compute Beta PDF
i = np.linspace(0, 1, 1000)
beta_pdf = beta.pdf(i, alpha, beta_param)

# Joint distributions for t=0 and t=1
joint_t0 = (1 - i) * beta_pdf
joint_t1 = i * beta_pdf

# Replace zeros with epsilon (to avoid log(0) errors)
joint_t1 = np.where(joint_t1 == 0, epsilon, joint_t1)

# Create a 2D grid for heatmap (rows: t=0 and t=1, columns: i)
X, Y = np.meshgrid(i, [0, 1])
Z = np.vstack([joint_t0, joint_t1])

# Plot heatmap with logarithmic color scale
plt.figure(figsize=(14, 4))
c = plt.pcolormesh(X, Y, Z, norm=LogNorm(vmin=epsilon, vmax=Z.max()), shading='auto', cmap='viridis')
plt.colorbar(c, label='$\\log(p(t, i))$', extend='min')

# Customize plot
plt.xlabel('$i$', fontsize=12)
plt.ylabel('$t$', fontsize=12)
plt.yticks([0, 1], ['0', '1'])
plt.title('Log-Scale Heatmap of Joint Distribution $p(t, i)$ (Beta(1, 19))', fontsize=14)
plt.tight_layout()
plt.show()
