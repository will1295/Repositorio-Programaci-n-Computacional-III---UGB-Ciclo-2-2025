from django.shortcuts import render,redirect
from .forms import ProductoForm
from .models import Producto

def home(request):
    return render(request,'home.html')

def verproductos(request):
    productos = Producto.objects.all()
    return render(request,'productos.html',{"productos":productos})

def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("productos")
    else:
        form = ProductoForm()

    return render(request,'crear_producto.html',{"form":form})