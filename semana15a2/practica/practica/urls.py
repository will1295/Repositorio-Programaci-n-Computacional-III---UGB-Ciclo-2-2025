from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.saludo),
    path('listado/',views.listado),
    path('seccion/<slug:seccion>',views.pagina2),
    path('inicio/<str:nombre>',views.usuario),
    path('dashboard/<str:usuario>',views.dashboard),
    path('producto/<int:id>',views.producto),
    path('libros/',views.Libros.as_view()),
    path('estudiantes/<str:estudiante>',views.Estudiantes.as_view()),
    path('profesores/<str:profesor>',views.Profesores.as_view()),
]
