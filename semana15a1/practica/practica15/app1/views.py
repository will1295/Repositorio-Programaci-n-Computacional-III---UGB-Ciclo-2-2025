from django.shortcuts import render

def inicio(request):
    return render(request,'inicio.html')

def zapatos(request):
    return render(request,'zapatos.html')