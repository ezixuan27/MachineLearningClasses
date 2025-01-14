#!/usr/bin/env python

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib as mpl

mpl.rcParams['savefig.directory'] = '/home/chieh/code/MachineLearningClasses/ML_2/1_multivariate_gaussian'

# Define the parameters for 4 Gaussians
means = [
	np.array([0, 0]),
	np.array([2, 2]), 
	np.array([-1.5, 1]),
	np.array([1, -2])  
]

covariances = [
	np.array([[2, 0], [0, 3]]),
	np.array([[2, 0], [0, 2]]),
	np.array([[1, 0], [0, 1]]),
	np.array([[1, 0], [0, 1]]) 
]

# Number of samples to generate from each distribution
num_samples = 800

# Generate samples and store them in a list
samples = []
for i in range(len(means)):
	# Generate samples from the i-th multivariate Gaussian distribution
	samples_i = np.random.multivariate_normal(means[i], covariances[i], num_samples)
	samples.append(samples_i)

# Combine all samples into a single array
all_samples = np.vstack(samples)

# Convert to a pandas DataFrame
df = pd.DataFrame(all_samples, columns=['x1', 'x2'])

# Save to a CSV file
df.to_csv('landscape.csv', index=False, float_format='%.3f')

print("Samples saved to 'multivariate_gaussian_samples.csv'")

# Plot a 3D histogram of the samples
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Create histogram bins
hist, xedges, yedges = np.histogram2d(df['x1'], df['x2'], bins=15)

# Construct arrays for the anchor positions of the bars
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, yedges[:-1] + 0.25, indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Construct arrays with the dimensions for the bars
dx = dy = 0.5 * np.ones_like(zpos)
dz = hist.ravel()

# Plot the 3D histogram
ax.bar3d(xpos, ypos, zpos, dx, dy, dz, shade=True, alpha=0.8)

# Set labels and title
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('Frequency')
ax.set_title('3D Histogram of Multivariate Gaussian Samples')

# Show the plot
plt.tight_layout()
plt.show()
