from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from veterinaria.models import *
from veterinaria.fomrs import *

def index(request):
    return render(request, 'veterinaria/index.html')

def empleados(request):
    titulo = 'Empleados'
    empleados= Empleados.objects.all()
    if request.method == 'POST':
        formulario = EmpleadosFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            empleado= Empleados(data['nombre'],data['apellido'],data['dni'],data['telefono'],data['cargo'],)
            
            empleado.save()

            formulario = EmpleadosFormulario()
            return render(request, 'veterinaria/empleados.html', {'formulario':formulario,'empleados':empleados})
            
    else:
        formulario = EmpleadosFormulario()

        return render(request, 'veterinaria/empleados.html', {'titulo':titulo,'formulario':formulario,'empleados':empleados})


def pacientes(request):
    titulo = 'Pacientes'
    pacientes= Pacientes.objects.all()
    if request.method == 'POST':
        formulario = PacientesFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            paciente= Pacientes(data['nombre'],data['apellido'],data['dni'],data['telefono'],data['nombre_mascota'],data['observacion'])
            
            paciente.save()

            formulario = PacientesFormulario()
            return render(request, 'veterinaria/pacientes.html', {'titulo':titulo,'formulario':formulario,'pacientes':pacientes})

    else:
        formulario = PacientesFormulario()

        return render(request, 'veterinaria/pacientes.html', {'titulo':titulo,'formulario':formulario,'pacientes':pacientes})

def productos(request):
    titulo = 'Productos'
    productos= Productos.objects.all()
    if request.method == 'POST':
        formulario = ProductosFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto= Productos(data['nombre'],data['precio'],data['stock'])
            
            producto.save()

            formulario = ProductosFormulario()
            return render(request, 'veterinaria/productos.html', {'titulo':titulo,'formulario':formulario,'productos':productos})
    else:
        formulario = ProductosFormulario()
        return render(request, 'veterinaria/productos.html',{'titulo':titulo,'formulario':formulario,'productos':productos})



def contacto(request):
    titulo = 'Contacto'
    contactos = Contacto.objects.all()
    
    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            contactos = Contacto(data['nombre'],data['apellido'],data['telefono'],data['email'],data['mensaje'])
            contactos.save()
            formulario = ContactoFormulario()
            return render(request, 'veterinaria/contacto.html', {'titulo':titulo,'formulario':formulario,'contactos':contactos})
    else:
        formulario = ContactoFormulario()
        
        return render(request, 'veterinaria/contacto.html',{"titulo":titulo ,"formulario":formulario,'contactos':contactos}) 


# ======================================================================================================
# ======================================================================================================


def buscarEmpleado(request):
    
    data = request.GET.get('dni',"")                        #Tengo el get de la url
    error = ""
    print(data)         #chequeo la data que me llega
    error = ''
    if data:
        try:
            empleado = Empleados.objects.filter(dni=data)   #filtro al empleado por el dni
            # print(empleado)
            return render (request, 'veterinaria/buscarEmpleados.html', {'empleado':empleado[0], "id":data})   #renderizo y mando el empleado que tiene que ser [0] poruqe manda una lista
        except Exception as exc:
            print(exc)
            error = 'No se encontro el empleado'

    return render(request, 'veterinaria/buscarEmpleados.html', {'error':error})






def buscarPaciente(request):
       
    data = request.GET.get('nombre_mascota')                        #Tengo el get de la url
    error = ""
    print(data)         #chequeo la data que me llega
    error = ''
    if data:
        try:
            pacientes = Pacientes.objects.filter(nombre_mascota__icontains=data)   #filtro al empleado por el dni
            print(pacientes)
            return render (request, 'veterinaria/buscarPaciente.html', {'pacientes':pacientes[0], "id":data})   #renderizo y mando el empleado que tiene que ser [0] poruqe manda una lista
        except Exception as exc:
            print(exc)
            error = 'No se encontro el paciente'

    return render(request, 'veterinaria/BuscarPaciente.html', {'error':error})


def buscarProducto(request):
    data = request.GET.get('id')                        
    error = ""
    print(data)         #chequeo la data que me llega
    if data:
        try:
            producto = Productos.objects.filter(id__icontains=data)
            print(producto)
            return render (request, 'veterinaria/buscarProducto.html', {'producto':producto[0], "id":data})

        except Exception as exc:
            print(exc)
            error = 'No se encontro el producto'

    return render(request, 'veterinaria/buscarProducto.html', {'error':error})
