from django.shortcuts import render,redirect
from .forms import ProductoForm
from django.http import HttpResponse
from .models import Producto

def home(request):
    return render(request,'home.html')

def ver_productos(request):
    productos = Producto.objects.all()
    return render(request,'verproductos.html',{"productos":productos})


def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("verproductos")
    else:
        form = ProductoForm()
    return render(request,"crear_producto.html",{"form":form})
