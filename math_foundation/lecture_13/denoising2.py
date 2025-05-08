#!/usr/bin/env python
import numpy as np
import matplotlib.pyplot as plt
from skimage import data, util, img_as_float

# Load grayscale image
image = img_as_float(data.camera())  # Already grayscale

# Corrupt image: add a black square
corrupted = image.copy()
x0, y0, size = 100, 100, 2 
corrupted[x0:x0+size, y0:y0+size] = 0

# Apply SVD
U, S, Vᵀ = np.linalg.svd(corrupted, full_matrices=False)

# Reconstruct using top k components
k = 300
S[k:] = 0
reconstructed = (U * S) @ Vᵀ

# Plot
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
axes[0].imshow(image, cmap='gray')
axes[0].set_title("Original")
axes[0].axis("off")

axes[1].imshow(corrupted, cmap='gray')
axes[1].set_title("Corrupted (Black Patch)")
axes[1].axis("off")

axes[2].imshow(reconstructed, cmap='gray')
axes[2].set_title(f"Reconstructed (Rank {k})")
axes[2].axis("off")

plt.tight_layout()
plt.show()

