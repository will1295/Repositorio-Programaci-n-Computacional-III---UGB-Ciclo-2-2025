from django.shortcuts import render,redirect
from .models import Producto,Categoria
from .forms import ProductoForm,CategoriaForm

def home(request):
    return render(request,"home.html")

def verproductos(request):
    productos = Producto.objects.all()
    return render(request,'verproductos.html',{"productos":productos})

def crearproducto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('verproductos')
    else:
        form = ProductoForm()
        return render(request,'crearproducto.html',{"form":form})
    

def vercategorias(request):
    categorias = Categoria.objects.all()
    return render(request,'vercategorias.html',{"categorias":categorias})

def crearcategoria(request):
    if request.method == "POST":
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vercategorias')
    else:
        form = CategoriaForm()
        return render(request,'crearcategoria.html',{"form":form})    