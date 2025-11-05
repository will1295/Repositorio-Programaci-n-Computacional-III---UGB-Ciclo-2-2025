from django.contrib import admin
from django.urls import path
from app1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.saludo),
    path('productos/',views.productos),
    path('perfil/',views.perfil),
    path('home/<str:nombre>',views.usuario),
    path('pagina1/<int:id>',views.registro),
    path('pagina2/<slug:seccion>',views.seccion),
    path('pagina3/<uuid:numeros>',views.secreto),
    path('saludo/', views.SaludoView.as_view(),name="saludo_clase"),
   # path('dashboard/', views.DashboardView.as_view(),name="dashboard_clase"),
    path('producto/<int:producto_id>', views.ProductoView.as_view(),name="producto_clase"),
]
