#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, util, img_as_float

# Load grayscale image
image = img_as_float(data.camera())

# Add black patch (simulate missing region)
corrupted = image.copy()
x0, y0, size = 40, 40, 3
corrupted[x0:x0+size, y0:y0+size] = 0


fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[1].imshow(corrupted, cmap='gray')
axes[1].set_title("Local Patch (Corrupted)")
axes[1].axis("off")


# Define crop size around corrupted region
pad = 80
x_start = max(x0 - pad, 0)
y_start = max(y0 - pad, 0)
x_end = min(x0 + size + pad, image.shape[0])
y_end = min(y0 + size + pad, image.shape[1])

# Crop patch around corrupted area
patch = corrupted[x_start:x_end, y_start:y_end]

# SVD on patch
U, S, Vᵀ = np.linalg.svd(patch, full_matrices=False)
k = 1
S[k:] = 0
patch_reconstructed = (U * S) @ Vᵀ

# Replace only the black region with corresponding portion from reconstruction
x_local = x0 - x_start
y_local = y0 - y_start
corrupted[x0:x0+size, y0:y0+size] = patch_reconstructed[x_local:x_local+size, y_local:y_local+size]

# Plot results
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Original")
axes[0].axis("off")

axes[2].imshow(corrupted, cmap='gray')
axes[2].set_title("Final Image (Inpainted Patch)")
axes[2].axis("off")

plt.tight_layout()
plt.show()

