#Abrir y guardar una imagen
from PIL import Image

imagen = Image.open("logo_ugb.webp")
imagen.show()

print("Formato: ",imagen.format)
print("Tamaño: ",imagen.size)
print("Modo de color: ",imagen.mode)

imagen.save("imagenes/logo.webp")