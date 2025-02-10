#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

# Parameters
alpha = 1.0    # Beta distribution parameter (heavily skewed toward 0)
beta = 19.0    # Beta distribution parameter
n_samples = 30000  # Number of samples

# Step 1: Sample p from Beta(alpha, beta)
p_values = [1,1,3,4,4]

# Step 2: Sample t from Bernoulli(p) for each p
bernoulli_samples = [0,0,1,1,1]

# Step 3: Create a 2D histogram (heatmap)
heatmap, xedges, yedges = np.histogram2d(
    p_values, 
    bernoulli_samples, 
    bins=[3, 2],  # 50 bins for p, 2 bins for t (0 and 1)
    range=[[1, 4], [-0.5, 1.5]]  # p: [0, 1], t: [-0.5, 1.5]
)
print(heatmap)

# Correct alignment: Ensure t=0 is at the bottom, t=1 at the top
heatmap = np.flipud(heatmap.T)  # Transpose and flip rows to align t=0 and t=1
print(heatmap)


# Plot the heatmap
plt.figure(figsize=(10, 4))
plt.imshow(
    heatmap, 
    extent=[0, 4, -0.5, 1.5],  # Axis limits (x: p, y: t)
    aspect="auto", 
    cmap="viridis", 
    origin="upper"  # Ensure t=0 is at the bottom
    #origin="lower"  # Ensure t=0 is at the bottom
)

# Customize the plot
plt.colorbar(label="Frequency")
plt.xlabel("p (Beta distribution)")
plt.ylabel("t (Bernoulli samples)")
plt.yticks([0, 1], ["0", "1"])  # Label y-axis with t=0 and t=1
plt.title("Heatmap of Ancestral Sampling (Beta(1,19) → Bernoulli)")

plt.show()
