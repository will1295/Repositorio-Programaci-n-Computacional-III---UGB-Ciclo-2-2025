from django import forms

class LoginForm(forms.Form):
    usuario = forms.CharField(label="Usuario")
    password = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput,
        min_length=4
    )