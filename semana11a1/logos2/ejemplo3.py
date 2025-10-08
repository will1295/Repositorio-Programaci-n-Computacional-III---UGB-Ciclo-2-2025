from PIL import Image,ImageFilter

imagen = Image.open("store.jpg")

imagen.filter(ImageFilter.CONTOUR).show()
imagen.filter(ImageFilter.DETAIL).show()
imagen.filter(ImageFilter.EDGE_ENHANCE).show()
imagen.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
imagen.filter(ImageFilter.EMBOSS).show()
imagen.filter(ImageFilter.FIND_EDGES).show()
imagen.filter(ImageFilter.SMOOTH).show()
imagen.filter(ImageFilter.SMOOTH_MORE).show()
imagen.filter(ImageFilter.BLUR).show()

