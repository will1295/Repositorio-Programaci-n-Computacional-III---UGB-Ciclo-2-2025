from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from django.contrib.auth.models import User

@login_required
def home(request):
    return render(request,'home.html')


def iniciar_sesion(request):

    mensaje = ""
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            usuario = form.cleaned_data["usuario"]
            password = form.cleaned_data["password"]
            user = authenticate(request,username=usuario,password=password)
            if user:
                login(request,user)
                return redirect("home")
            else:
                return render(request,"login.html",{
                    "form":form,
                    "error":"Credenciales incorrectas"
                })
    else:
        form = LoginForm()
        return render(request,"login.html",{"form":form,"mensaje":mensaje})    

def registrar_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            return render(request,"registro.html",{
                "error":"Las contraseñas no coinciden"
            })
        
        if User.objects.filter(username=username).exists():
            messages.error(request,"El usuario ya existe, intenta con otro")
            return redirect("registro")

        user = User.objects.create_user(username=username,password=password)
        user.save()
        messages.success(request,"Usuario creado correctamente") 
        return redirect("login")  

    return render(request,"registro.html")     


def cerrar_sesion(request):
    logout(request)
    return redirect("login")


def crear_usuario(request):
    request.session["nombre_usuario"] = "Invitado"
    return HttpResponse("Nombre de usuario almacenado")
 
def leer_usuario(request):
    nombre = request.session.get("nombre_usuario","No existe este usuario")
    return HttpResponse(f"Usuario: {nombre}")

def eliminar_usuario(request):
    if "nombre_usuario" in request.session:
        del request.session["nombre_usuario"]
        return HttpResponse("Se ha eliminado el usuario")

def limpiar_sesion(request):
    request.session.flush()
    return HttpResponse("La sesion ha sido eliminada")