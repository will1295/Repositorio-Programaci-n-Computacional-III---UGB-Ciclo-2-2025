from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    fkcateg = models.ForeignKey(Categoria,on_delete=models.CASCADE,default=1)

    def __str__(self):
        return f"Nombre del producto: {self.nombre}"

