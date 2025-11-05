from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludo(request):
    return HttpResponse("¡Bievenidos al Himalaya!, ¿Helado?")

def pagina(request):
    return render(request,'pagina.html')