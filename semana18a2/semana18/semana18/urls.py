from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.inicio,name = 'home'),
    path('guardar/',views.guardar_nombre),
    path('leer/',views.leer_nombre),
    path('eliminar/',views.eliminar_nombre),
    path('contador/',views.contador_visitas),
    path('login/',views.iniciar_sesion, name='login'),
    path('registro/',views.crear_usuario,name="registro"),
    path('logout/',views.cerrar_sesion,name='logout')
]
