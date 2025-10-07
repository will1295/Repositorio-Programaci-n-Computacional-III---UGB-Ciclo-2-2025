from PIL import Image
from urllib.request import urlopen

url = "https://ugb.edu.sv/wp-content/uploads/2024/10/UGB_LOGO_AZUL-e1733330447419.png"
imagen = Image.open(urlopen(url))
imagen.show()