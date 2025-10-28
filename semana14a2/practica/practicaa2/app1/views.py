from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("¡Bievenidos al Himayala!, ¿Helado?")

def info(request):
    return render(request,"datos.html")