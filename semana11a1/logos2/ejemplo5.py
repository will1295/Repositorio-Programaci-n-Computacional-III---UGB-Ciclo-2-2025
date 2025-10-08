from PIL import Image,ImageDraw,ImageFont

imagen = Image.open("edificio.webp")
#imagen.thumbnail((200,200))

letras = ImageDraw.Draw(imagen)
font = ImageFont.truetype("arial.ttf",size=100)

letras.text((1000,1000),"Texto con Pillow",font=font, fill=(92,117,214))
imagen.show()
