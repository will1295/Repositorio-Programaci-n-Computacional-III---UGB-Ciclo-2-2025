#filtros
from PIL import Image,ImageFilter

imagen = Image.open("ugb_store.jpg")

contorno = imagen.filter(ImageFilter.CONTOUR)
contorno.show()
detallado = imagen.filter(ImageFilter.DETAIL)
detallado.show()
edges = imagen.filter(ImageFilter.EDGE_ENHANCE)
edges.show()
edges2 = imagen.filter(ImageFilter.EDGE_ENHANCE_MORE)
edges2.show()
relieve = imagen.filter(ImageFilter.EMBOSS)
relieve.show()
edges3 = imagen.filter(ImageFilter.FIND_EDGES)
edges3.show()
suavizado = imagen.filter(ImageFilter.SMOOTH)
suavizado.show()
suavizado2 = imagen.filter(ImageFilter.SMOOTH_MORE)
suavizado2.show()