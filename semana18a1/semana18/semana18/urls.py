from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('crearusuario/',views.crear_usuario),
    path('leerusuario/',views.leer_usuario),
    path('eliminarusuario/',views.eliminar_usuario),
    path('limpiarsesion/',views.limpiar_sesion),
    path('login/',views.iniciar_sesion,name="login"),
    path('logout/',views.cerrar_sesion,name="logout"),
    path('registro/',views.registrar_usuario,name="registro")
]
