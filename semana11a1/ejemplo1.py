from PIL import Image
import os

imagen = Image.open("logo_ugb.webp")
#imagen.show()

imagen.save("logos/logo.webp")

if not os.path.exists("logos2"):
    os.mkdir("logos2")

imagen.save("logos2/logo.webp")
