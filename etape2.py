import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("photo.jpg")
print(img.shape)
print(img.dtype)
print(img.min(), img.max())

plt.imshow(img)
plt.show()