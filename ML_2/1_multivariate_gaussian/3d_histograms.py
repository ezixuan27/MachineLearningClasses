#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create sample data
# Generate random data for demonstration
np.random.seed(42)
x = np.random.normal(0, 2, 1000)
y = np.random.normal(0, 2, 1000)

# Create the 3D histogram
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Create histogram data
hist, xedges, yedges = np.histogram2d(x, y, bins=20)
xpos, ypos = np.meshgrid(xedges[:-1], yedges[:-1], indexing="ij")

# Convert to 1D arrays
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Convert histogram data to match dimensions
dx = dy = (xedges[1] - xedges[0])
dz = hist.ravel()

# Create the 3D bars
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')

# Customize the plot
ax.set_xlabel('X axis')
ax.set_ylabel('Y axis')
ax.set_zlabel('Frequency')
ax.set_title('3D Histogram of 2D Normal Distribution')

# Add a colorbar
norm = plt.Normalize(dz.min(), dz.max())
colors = plt.cm.viridis(norm(dz))
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, color=colors, zsort='average')

plt.show()
