#Cambios de tamanio
from PIL import Image

foto = Image.open("edificio.webp")
#print("Tamaño: ",foto.size)
cambio = foto.resize((300,200))
#cambio.show()

#foto.thumbnail((200,200))
#foto.show()

#Rotacion
rotada = foto.rotate(90)
#rotada.show()

volteado = foto.transpose(Image.FLIP_LEFT_RIGHT)
volteado.show()

volteado2 = foto.transpose(Image.FLIP_TOP_BOTTOM)
volteado2.show()