from django.shortcuts import render

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def empleados(request):
    return render(request, 'empleados.html')


def pacientes(request):
    return render(request, 'pacientes.html')

def productos(request):
    return render(request, 'productos.html')

def prueba(request):
    return render(request, 'padre.html')
