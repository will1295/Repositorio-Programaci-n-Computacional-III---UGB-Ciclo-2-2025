from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('producto/',views.verproductos,name='productos'),
    path('producto/nuevo/',views.crear_producto,name='crearproducto')
]
