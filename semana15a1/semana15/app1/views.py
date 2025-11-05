from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin

#Vistas basadas en funciones

def saludo(request):
    return HttpResponse("Hola Mundo!")

def pagina(request):
    return render(request,'pagina1.html')

def pagina2(request):

    productos = [
        {'nombre':'cocacola','precio':2.00},
        {'nombre':'aceite','precio':2.60},
        {'nombre':'azucar','precio':0.50},
        {'nombre':'sal','precio':0.30},
    ]

    datos = {
        'nombre':'Juan',
        'productos':productos
    }
    return render(request,'pagina2.html',datos)

@require_http_methods(["GET"])
def saludo_user(request,nombre):
    return HttpResponse(f"Hola {nombre}")

@login_required
def producto(request,id):
    if(id==1):
        producto = "Manzana"
    elif(id==2):
        producto = "Zanahoria"
    return HttpResponse(f"Nombre del producto: {producto}")


#Vistas basadas en clases

class SaludoClass(View):
    def get(self,request):
        return HttpResponse("Vista basada en clases")

#@method_decorator(login_required,name='dispatch')
class UsuarioClass(LoginRequiredMixin,View):
    def get(self,request,nombre):
        return HttpResponse(f"Bienvenido {nombre}")


