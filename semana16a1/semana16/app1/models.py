from django.db import models


class Instituto(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(20)

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    grado = models.CharField(max_length=50)
    seccion = models.CharField(max_length=1)
    turno = models.CharField(max_length=20)
    fkinst = models.ForeignKey(Instituto,on_delete=models.CASCADE,null=True)

class IdentifEstudiantil(models.Model):
    codigo = models.CharField(max_length=10)
    fkest = models.OneToOneField(Estudiante,on_delete=models.CASCADE)
    fecha_emision = models.DateField()

class Materia(models.Model):
    codigomateria = models.CharField(max_length=10) 
    nombre = models.CharField(max_length=50)
    fkest = models.ManyToManyField(Estudiante)
    
