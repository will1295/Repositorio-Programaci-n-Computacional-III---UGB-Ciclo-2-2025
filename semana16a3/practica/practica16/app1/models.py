from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    direccion = models.TextField()
    telefono = models.CharField(max_length=15,unique=True)
    email = models.EmailField(unique=True)

class Pedido(models.Model):
    producto = models.CharField(max_length=100)
    cantidad = models.IntegerField()
    total = models.DecimalField(max_digits=10,decimal_places=2)
    cliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)
    fpedido = models.DateTimeField()
