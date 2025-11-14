from django.shortcuts import render
from .models import Cliente,Pedido

def listcli(request):
        #SELECT * FROM Cliente
    clientes = Cliente.objects.all()
    return render(request,"listaclientes.html",{"clientes":clientes})

def listpedidos(request):
    pass
