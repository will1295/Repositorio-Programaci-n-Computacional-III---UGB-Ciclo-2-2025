from PIL import Image,ImageDraw,ImageFont

imagen = Image.open("edificio.webp")
#imagen.thumbnail((200,200))

draw = ImageDraw.Draw(imagen)
fuente = ImageFont.truetype("arial.ttf",size=100)

draw.text((100,100),"Texto aqui",font=fuente,fill=(39,56,245))
imagen.show()
