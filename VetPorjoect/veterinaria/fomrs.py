
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from veterinaria.models import *
class EmpleadosFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.IntegerField()
    telefono = forms.IntegerField()
    cargo = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=254)
    imagen = forms.ImageField()

    
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


class PostForm(forms.ModelForm):
    
    class Meta:
        model= Post
        fields=('titulo','autor','contenido')

        widgets={
            'titulo':forms.TextInput(attrs={'class':'form-control'}),
            'autor':forms.TextInput(attrs={'class':'form-control','value':'','id':'autor','type':'hidden'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
          }


class ComentForm(forms.ModelForm):
    
    class Meta:
        model=Comentario
        fields=('autor','contenido')

        widgets={
            'autor':forms.TextInput(attrs={'class':'form-control','value':'','id':'autor','type':'hidden'}),
            'contenido':forms.Textarea(attrs={'class':'form-control'}),
        }
