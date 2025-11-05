from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.saludo),
    path('pagina/',views.pagina),
    path('pagina2/',views.pagina2),
    path('usuario/<str:nombre>',views.saludo_user),
    path('producto/<int:id>',views.producto),
    path('saludo/',views.SaludoClass.as_view()),
    path('user/<str:nombre>',views.UsuarioClass.as_view())
]
