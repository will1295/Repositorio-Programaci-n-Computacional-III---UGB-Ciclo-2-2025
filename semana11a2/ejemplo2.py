from PIL import Image,ImageFilter
imagen = Image.open("edificio.webp")

#Rotaciones
rotacion = imagen.rotate(90)
#rotacion.show()
rotacion2 = imagen.rotate(180)
#rotacion2.show()
rotacion3 = imagen.rotate(270)
#rotacion3.show()

imagen.transpose(Image.FLIP_LEFT_RIGHT).show()
imagen.transpose(Image.FLIP_TOP_BOTTOM).show()


#Filtros

#img_contor = imagen.filter(ImageFilter.CONTOUR).show()
#img_detail = imagen.filter(ImageFilter.DETAIL).show()
#img_edge = imagen.filter(ImageFilter.EDGE_ENHANCE).show()
#img_edgem = imagen.filter(ImageFilter.EDGE_ENHANCE_MORE).show()
#img_emboss = imagen.filter(ImageFilter.EMBOSS).show()
#img_findedg = imagen.filter(ImageFilter.FIND_EDGES).show()
#img_smooth = imagen.filter(ImageFilter.SMOOTH).show()
#img_smoothm = imagen.filter(ImageFilter.SMOOTH_MORE).show()









