from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.CharField(max_length=100,unique=True)
    telefono = models.IntegerField(unique=True)
    dui = models.CharField(max_length=10,unique=True)

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    total = models.DecimalField(max_digits=10,decimal_places=2)