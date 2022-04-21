import email
from django import forms
import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class EmpleadosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    cargo = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)

    
class PacientesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    nombre_mascota = forms.CharField(max_length=50)
    observacion =  forms.CharField(max_length=300)
    email = forms.EmailField()
   

class ProductosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    precio = forms.IntegerField()
    stock = forms.IntegerField()
  

class ContactoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    telefono = forms.IntegerField()
    mensaje = forms.CharField(max_length=300)


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña 1')
    password2 = forms.CharField(widget=forms.PasswordInput , label='Contraseña 2')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_text = {k : '' for k in fields}

class UsuarioEditForm(UserCreationForm):

    email = forms.EmailField()
    password1 = forms.CharField(label='Contrasenia 1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Contrasenia 2', widget=forms.PasswordInput)

    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")

    class Meta:
        model = User
        fields = ['first_name','last_name','email', 'password1', 'password2']
        help_text = { k: "" for k in fields}



class AvatarFormulario(forms.Form):

    imagen = forms.ImageField()