from django.shortcuts import render

# Create your views here.

def inicio(request):
    return render(request,'inicio.html')

def laptops(request):
    return render(request,'laptops.html')