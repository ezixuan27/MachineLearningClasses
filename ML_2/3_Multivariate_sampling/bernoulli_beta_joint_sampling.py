#!/usr/bin/env python

import matplotlib as mpl
mpl.rcParams['savefig.directory'] = '/home/chieh/code/MachineLearningClasses/ML_2/3_Multivariate_sampling'

import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.0    # Beta distribution parameter (heavily skewed toward 0)
beta = 19.0    # Beta distribution parameter
n_samples = 30000  # Number of samples

# Step 1: Sample p from Beta(alpha, beta)
p_values = np.random.beta(alpha, beta, n_samples)

# Step 2: Sample t from Bernoulli(p) for each p
bernoulli_samples = np.random.binomial(1, p_values)

# Step 3: Create a 2D histogram (heatmap)
heatmap, xedges, yedges = np.histogram2d(
    p_values, 
    bernoulli_samples, 
    bins=[100, 2],  # 50 bins for p, 2 bins for t (0 and 1)
    range=[[0, 0.1], [-0.5, 1.5]]  # p: [0, 1], t: [-0.5, 1.5]
)

#	This matrix, each value is a single pixel
heatmap = heatmap.T  # Transpose and flip rows to align t=0 and t=1

# Plot the heatmap
plt.figure(figsize=(10, 4))
plt.imshow(
    heatmap, 
    extent=[0, 1, -0.5, 1.5],  # Axis limits (x: p, y: t)
    aspect="auto", 
    cmap="viridis", 
    origin="upper"  # Ensure t=0 is at the bottom
)

# Customize the plot
plt.colorbar(label="Frequency")
plt.xlabel("p (Beta distribution)")
plt.ylabel("t (Bernoulli samples)")
plt.yticks([0, 1], ["0", "1"])  # Label y-axis with t=0 and t=1
plt.title("Heatmap of Ancestral Sampling (Beta(1,19) → Bernoulli)")

plt.show()
