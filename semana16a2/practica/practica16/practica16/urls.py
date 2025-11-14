from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.listclientes),
    path('pedidos/',views.listpedidos)

]
