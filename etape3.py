import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("photo.jpg")

haut = img[0:2500, :, :]        # découper : les 2500 premières lignes
miroir = img[:, ::-1, :]        # miroir : colonnes à l'envers
gris = img.mean(axis=2)         # noir et blanc : moyenne des 3 couleurs
negatif = 255 - img             # négatif : on inverse les valeurs

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes[0, 0].imshow(haut)
axes[0, 0].set_title("Découpée")
axes[0, 1].imshow(miroir)
axes[0, 1].set_title("Miroir")
axes[1, 0].imshow(gris, cmap="gray")
axes[1, 0].set_title("Noir et blanc")
axes[1, 1].imshow(negatif)
axes[1, 1].set_title("Négatif")
plt.savefig("resultat_transformations.png", dpi=120, bbox_inches="tight")
plt.show()
