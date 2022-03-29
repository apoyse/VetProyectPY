import email
from django import forms
import datetime

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
