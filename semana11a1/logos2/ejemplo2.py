from PIL import Image

imagen = Image.open("edificio.webp")

print(imagen.size)

#imagen.thumbnail((200,200))
#imagen.show()
#reducida = imagen.resize((100,400))
#reducida.show()

imagen.rotate(90).show()
imagen.rotate(180).show()
imagen.rotate(270).show()

imagen.transpose(Image.Transpose.FLIP_LEFT_RIGHT).show()
imagen.transpose(Image.Transpose.FLIP_TOP_BOTTOM).show()