import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("photo.jpg")
gris = img.mean(axis=2)

# Pixelisation : on garde 1 pixel sur 60
petit = img[::60, ::60, :]

# Contours : différence entre pixels voisins
dx = np.abs(np.diff(gris, axis=1))
dy = np.abs(np.diff(gris, axis=0))
contours = dx[:-1, :] + dy[:, :-1]

fig, axes = plt.subplots(1, 2, figsize=(12, 7))
axes[0].imshow(petit, interpolation="nearest")
axes[0].set_title("Pixelisée")
axes[1].imshow(contours, cmap="gray", vmax=60)
axes[1].set_title("Contours")
plt.savefig("resultat_contours.png", dpi=120, bbox_inches="tight")
plt.show()
