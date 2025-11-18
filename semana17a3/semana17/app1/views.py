from django.shortcuts import render,redirect
from .forms import ProductoForm,CategoriaForm
from .models import Producto,Categoria

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


def vercategorias(request):
    categorias = Categoria.objects.all()
    return render(request,'categorias.html',{"categorias":categorias})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("categorias")
    else:
        form = CategoriaForm()

    return render(request,'crear_categoria.html',{"form":form})