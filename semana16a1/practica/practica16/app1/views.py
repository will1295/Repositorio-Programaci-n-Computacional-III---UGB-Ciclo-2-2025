from django.shortcuts import render
from .models import Cliente,Pedido

def verclientes(request):
    clientes = Cliente.objects.all()
    return render(request,'listaclientes.html',{"clientes":clientes})

def verpedidos(request):
    pass

