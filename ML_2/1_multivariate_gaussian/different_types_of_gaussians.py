#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import multivariate_normal
import matplotlib as mpl

mpl.rcParams['savefig.directory'] = '/home/chieh/code/MachineLearningClasses/ML_2/1_multivariate_gaussian'


# Define the means and covariance matrices
mean = np.array([0, 0])

cov1 = np.array([[0.1, 0], [0, 2]])
cov2 = np.array([[2, 0], [0, 0.1]])
cov3 = np.array([[0.3, 0], [0, 0.3]])
cov4 = np.array([[2, 0], [0, 2]])


#cov1 = np.array([[0.1, 0], [0, 2]])
#cov2 = np.array([[2, 0], [0, 0.1]])
#cov3 = np.array([[1, 0.9], [0.9, 1]])
#cov4 = np.array([[1, -0.9], [-0.9, 1]])

#cov1 = np.array([[1, 0.9], [0.9, 1]])
#cov2 = np.array([[0.05, 0], [0, 4]])
#cov3 = np.array([[1, 0], [0, 1]])

# Create a grid of points
x, y = np.mgrid[-5:5:.1, -5:5:.1]
pos = np.dstack((x, y))

# Generate the Gaussian distributions
rv1 = multivariate_normal(mean, cov1)
rv2 = multivariate_normal(mean, cov2)
rv3 = multivariate_normal(mean, cov3)
rv4 = multivariate_normal(mean, cov4)

# Calculate the probability density function (PDF) for each distribution
z1 = rv1.pdf(pos)
z2 = rv2.pdf(pos)
z3 = rv3.pdf(pos)
z4 = rv4.pdf(pos)

# Create the subplots
#fig, (ax1, ax2, ax3, ax4) = plt.subplots(1, 4, figsize=(20, 5))
fig, (ax1, ax2, ax3, ax4) = plt.subplots(4, 1, figsize=(5, 20))

# Plot the heat maps
im1 = ax1.imshow(z1, extent=[-5, 5, -5, 5], origin='lower', cmap='viridis')
ax1.set_title('$\Sigma_1$')
#ax1.set_title('Generalized Multivariate Gaussian')
ax1.set_xlabel('Xₗ')
ax1.set_ylabel('Xշ')

im2 = ax2.imshow(z2, extent=[-5, 5, -5, 5], origin='lower', cmap='viridis')
ax2.set_title('$\Sigma_2$')
#ax2.set_title('Product Of Gaussians')
ax2.set_xlabel('Xₗ')
ax2.set_ylabel('Xշ')

im3 = ax3.imshow(z3, extent=[-5, 5, -5, 5], origin='lower', cmap='viridis')
ax3.set_title('$\Sigma_3$')
#ax3.set_title('Spherical Gaussian')
ax3.set_xlabel('Xₗ')
ax3.set_ylabel('Xշ')

im4 = ax4.imshow(z4, extent=[-5, 5, -5, 5], origin='lower', cmap='viridis')
ax4.set_title('$\Sigma_4$')
ax4.set_xlabel('Xₗ')
ax4.set_ylabel('Xշ')



# Add colorbars
#fig.colorbar(im1, ax=ax1)
#fig.colorbar(im2, ax=ax2)
#fig.colorbar(im3, ax=ax3)

# Show the plot
plt.tight_layout()
plt.show()
