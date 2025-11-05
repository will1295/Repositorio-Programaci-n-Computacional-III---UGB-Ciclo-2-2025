from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from datetime import datetime

#Vistas basadas en funciones (FBV)

def saludo(request):
    return HttpResponse("Vista basada en funciones")

def usuario(request,nombre):
    return HttpResponse(f"Bievenido al sistema {nombre}")

def registro(request,id):
    return HttpResponse(f"Numero de registro {id}")

def seccion(request,seccion):
    return HttpResponse(f"{seccion}")

def secreto(request,numeros):
    return HttpResponse(f"Codigo del recurso{numeros}")

def productos(request):

    productos = [
        {'nombre':'Coca-cola','precio':2.00},
        {'nombre':'Sal de mesa','precio':0.25},
        {'nombre':'Azucar libra','precio':1.25}
    ]

    datos = {
        'empleado':'Juanito',
        'log':datetime.now(),
        'productos':productos

    }
    return render(request,'inicio.html',datos)

class SaludoView(View):
    def get(self,request):
        return HttpResponse("Vista basada en clases")
    
class ProductoView(View):
    def get(self,request,producto_id):
        return HttpResponse(f"Id del producto vendido {producto_id}")    
    
#@login_required
@require_http_methods(['GET'])
def perfil(request):
    return HttpResponse("Bienvenido a su perfil!")    


#@method_decorator(login_required,name='dispatch')
#class DashboardView(PermissionRequiredMixin,View):
#    permission_required='app.borrar_modelo'
#    def get(self,request):
#        return HttpResponse("Bienvenido al panel de administrador")