from django.db import models

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.TextField(null=True)
    telefono = models.IntegerField()
    fnacimiento = models.DateField()

class Perfil(models.Model):
    ident = models.CharField(max_length=10)
    usuario = models.OneToOneField(Usuario,on_delete=models.CASCADE)

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    nacionalidad = models.CharField(max_length=100)

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.ForeignKey(Autor,on_delete=models.CASCADE)

class Categorias(models.Model):
    nombre = models.CharField(max_length=100)
    libro = models.ManyToManyField(Libro)