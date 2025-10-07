from PIL import Image
imagen = Image.open("logo_ugb.webp")
#imagen.show()
#imagen.save("imagenes/logo1.webp")

print(f"Extension de la imagen: {imagen.format}")
print(f"La imagen tiene este tamaño: {imagen.size}")
print(f"Colores: {imagen.mode}")

cambiada = imagen.resize((200,100))
cambiada.show()