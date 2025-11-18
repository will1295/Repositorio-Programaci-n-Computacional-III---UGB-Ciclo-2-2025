from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    codigocli = models.CharField(max_length=10)
    telefono = models.CharField(max_length=9)
    direccion = models.TextField()

class Pedido(models.Model):
    codigopedido = models.CharField(max_length=10)
    fechaentrega = models.DateTimeField()
    total = models.DecimalField(max_digits=10,decimal_places=2)
    fkcliente = models.ForeignKey(Cliente,on_delete=models.CASCADE)