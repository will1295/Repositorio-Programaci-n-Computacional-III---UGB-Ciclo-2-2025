from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def saludo(request):
    return HttpResponse("Hola Mundo!")

def pagina(request):
    return render(request,"pagina1.html")
