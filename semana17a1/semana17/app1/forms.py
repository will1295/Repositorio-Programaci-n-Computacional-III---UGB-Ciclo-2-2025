from django import forms
from .models import Producto,Categoria

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ["codigo","nombre","precio","stock","fkcat"]

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ["nombre","descripcion"]        