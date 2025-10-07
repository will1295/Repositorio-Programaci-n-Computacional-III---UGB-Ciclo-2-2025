import matplotlib.pyplot as plt
from PIL import Image

imagen = Image.open("logo_ugb.webp")

plt.imshow(imagen)
plt.axis("off")
plt.title("Imagen con Matplotlib")
#plt.show()

escala_gris = imagen.convert("L")
fig,ax = plt.subplots(1,2,figsize=(8,4))
ax[0].imshow(imagen)
ax[0].set_title("Original")
ax[1].imshow(escala_gris,cmap="gray")
ax[1].set_title("Grises")
plt.show()