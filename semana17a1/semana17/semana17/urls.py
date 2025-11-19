from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('productos/',views.verproductos,name='verproductos'),
    path('productos/nuevo',views.crearproducto,name="crearproducto"),
    path('categorias/',views.vercategorias,name='vercategorias'),
    path('categorias/nuevo',views.crearcategoria,name="crearcategoria")
]
