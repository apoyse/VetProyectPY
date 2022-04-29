from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(widget=forms.PasswordInput, label='Contraseña 1')
    password2 = forms.CharField(widget=forms.PasswordInput , label='Contraseña 2')
    first_name = forms.CharField(label="Nombre")
    last_name = forms.CharField(label="Apellido")
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2','first_name','last_name']
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

