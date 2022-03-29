from django.urls import path
from veterinaria.views import *


urlpatterns = [
    path('', index, name='index'),
    
    path('pacientes/', pacientes, name='pacientes'),
   
    path('productos/', productos, name='productos'),
    path('empleados/', empleados, name='empleados'),
    path('contacto/', contacto, name='contacto'),
    path('buscarPaciente/', buscarPaciente, name='buscarPaciente'),
   
    path('buscarProducto/', buscarProducto, name='buscarProducto'),
    path('buscarEmpleado/', buscarEmpleado, name='buscarEmpleado'),
]