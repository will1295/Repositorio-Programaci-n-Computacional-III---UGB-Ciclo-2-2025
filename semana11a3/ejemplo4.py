#Agregar texto basico

from PIL import Image,ImageDraw,ImageFont

edificio = Image.open("edificio.webp")
dibujo = ImageDraw.Draw(edificio)
fuente = ImageFont.truetype("arial.ttf",size=100)

texto = "Edificio Innova"
medidas = dibujo.textbbox((0,0),texto,font=fuente)
anchotext = medidas[2] - medidas[0]
altotext = medidas[3] - medidas[1]
anchoimg,altoimg = edificio.size

x = (anchoimg-anchotext)/2
y = (altoimg-altotext)/2

dibujo.text((x,y),texto,fill=(255,0,0),font=fuente)
edificio.show()

