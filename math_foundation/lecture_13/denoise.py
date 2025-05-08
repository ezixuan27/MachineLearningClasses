#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from skimage import color, data, util
from skimage.metrics import peak_signal_noise_ratio as psnr

# Load the original image
original = color.rgb2gray(data.astronaut())
original = util.img_as_float(original)

# Add Gaussian noise
noisy = util.random_noise(original, mode='s&p', amount=0.05)
#noisy = util.random_noise(original, mode='gaussian', var=0.01)

# Perform SVD
U, S, Vt = np.linalg.svd(noisy, full_matrices=False)

# Keep only the top k singular values
k = 50
S_denoised = np.zeros_like(S)
S_denoised[:k] = S[:k]
S_matrix = np.diag(S_denoised)

# Reconstruct the image
denoised = np.dot(U, np.dot(S_matrix, Vt))

# Display the images
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(original, cmap='gray')
axes[0].set_title('Original Image')
axes[0].axis('off')

axes[1].imshow(noisy, cmap='gray')
axes[1].set_title('Noisy Image')
axes[1].axis('off')

axes[2].imshow(denoised, cmap='gray')
axes[2].set_title('Denoised Image (SVD)')
axes[2].axis('off')

plt.show()

# Calculate PSNR
print(f'PSNR of Noisy Image: {psnr(original, noisy):.2f} dB')
print(f'PSNR of Denoised Image: {psnr(original, denoised):.2f} dB')

