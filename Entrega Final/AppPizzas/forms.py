from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Create your models here.
class PizzaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    tamaño = forms.CharField(max_length=30)
    masa = forms.CharField(max_length=30)
    ingrediente1 = forms.CharField(max_length=30)
    ingrediente2 = forms.CharField(max_length=30)
    ingrediente3 = forms.CharField(max_length=30)
    ingrediente4 = forms.CharField(max_length=30)

class CreadorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    edad =  forms.IntegerField()
    correo = forms.EmailField()

class AsesorFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    cod_ases =  forms.IntegerField()
    correo = forms.EmailField()

class UsuarioRegistro(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username","email","first_name","last_name","password1","password2"]

class EditarUsuario(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Repetir la contraseña", widget=forms.PasswordInput)
    first_name = forms.CharField(label="Ingrese su nombre")
    last_name = forms.CharField(label="Ingrese su apellido")
    class Meta:
        model = User
        fields = ["email","password1","password2","first_name","last_name"]
