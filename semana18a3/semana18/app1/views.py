from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib import messages

@login_required
def pagina_principal(request):
    return render(request,"inicio.html")


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

def crear_usuario(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        password2 = request.POST.get("password2")

        if password != password2:
            return render(request,"registro.html",{
                "error":"Las contraseñas no coinciden"
            })

        if User.objects.filter(username=username).exists():
            messages.error(request,"El usuario ya existe")
            return redirect("registro")
        
        user = User.objects.create_user(username=username,
                                        password=password)
        user.save()
        messages.success(request,"Usuario creado correctamente")
        return redirect("login")
    
    return render(request,"registro.html")
        
def cerrar_sesion(request):
    logout(request)
    return redirect("login")

def guardar_nombre(request):
    request.session["nombre_usuario"] = "Invitado"
    return HttpResponse("El nombre de usuario ha sido almacenado")

def leer_nombre(request):
   nombre = request.session.get("nombre_usuario","No existe en la sesion")
   return HttpResponse(f"El nombre almacenado es: {nombre}")

def eliminar_nombre(request):
    if "nombre_usuario" in request.session:
        del request.session["nombre_usuario"]
    return HttpResponse("Se ha eliminado el usuario")

def limpiar_sesion(request):
    request.session.flush()
    return HttpResponse("Se ha eliminado toda la sesion")

def contador_visitas(request):
    visitas = request.session.get("visitas",0)
    visitas += 1
    request.session["visitas"] = visitas
    return render(request,"contador.html",{"visitas":visitas})



