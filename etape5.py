import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("photo.jpg")
gris = img.mean(axis=2)
petit = gris[::4, ::4]

U, S, Vt = np.linalg.svd(petit, full_matrices=False)

def compresser(k):
    return U[:, :k] @ np.diag(S[:k]) @ Vt[:k, :]

hauteur, largeur = petit.shape
fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(petit, cmap="gray")
axes[0, 0].set_title("Originale")

for ax, k in zip([axes[0, 1], axes[1, 0], axes[1, 1]], [5, 20, 80]):
    ax.imshow(compresser(k), cmap="gray")
    pourcent = 100 * k * (hauteur + largeur + 1) / (hauteur * largeur)
    ax.set_title(f"k = {k} ({pourcent:.0f} % des données)")
plt.savefig("resultat_compression.png", dpi=120, bbox_inches="tight")
plt.show()