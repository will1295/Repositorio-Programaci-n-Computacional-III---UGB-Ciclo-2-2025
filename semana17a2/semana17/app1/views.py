from django.shortcuts import render,redirect
from .forms import ProductoForm,CategoriaForm
from django.http import HttpResponse
from .models import Producto,Categoria

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


def ver_categorias(request):
    categorias = Categoria.objects.all()
    return render(request,'vercategorias.html',{"categorias":categorias})


def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("vercategorias")
    else:
        form = CategoriaForm()
    return render(request,"crear_categoria.html",{"form":form})
