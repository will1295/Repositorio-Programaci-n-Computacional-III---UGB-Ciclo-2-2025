from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin




#Views basadas en funciones (FBV)

def saludo(request):
    return HttpResponse("Views basadas en funciones")

def usuario(request,nombre):
    return HttpResponse(f"Bienvenido al sistema {nombre}")

def producto(request,id):
    return HttpResponse(f"Estas viendo el producto con id {id}")

#@login_required
@require_http_methods(["GET"])
def dashboard(request,usuario):
    return HttpResponse(f"Bienvenido admin: {usuario}")

def listado(request):

    productos = [
       {'producto':'Coca-cola','precio':2.00},
       {'producto':'Azucar','precio':1.10},
       {'producto':'Sal','precio':0.25},
       {'producto':'Aceite X','precio':1.35}
    ]

    datos = {
        'empleado':'Luis Hernandez',
        'area':'Informatica',
        'productos':productos
    }

    return render(request,'pagina1.html',datos)

def pagina2(request,seccion):
    return HttpResponse(seccion)

#Views basadas en clases

class Libros(View):
    def get(self,request):
        return HttpResponse("Pagina inicial de libros")


class Estudiantes(View):
    def get(self,request,estudiante):
        return HttpResponse(f"Bienvenido al sistema de notas {estudiante}")

#@method_decorator(login_required,name="dispatch")
#class Profesores(View):
#    def get(self,request,profesor):
#        return HttpResponse(f"Bienvenido al sistema de notas {profesor}")

class Profesores(LoginRequiredMixin,View):
    login_url = '/login/'
    def get(self,request,profesor):
        return HttpResponse(f"Bienvenido al sistema de notas {profesor}")
