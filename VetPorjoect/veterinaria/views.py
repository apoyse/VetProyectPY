
from django.shortcuts import render, HttpResponse
from django.shortcuts import render
from veterinaria.models import *
from veterinaria.fomrs import *

#Vistas Basasadas en clase
from django.views.generic import ListView #clase basada en vistas
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView


#User Login

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from usuario.views import *



def no_template(request):
    return HttpResponse("<h1> Lo siento. No hay template aun </h1>")

def index(request):
    imagen = avatar(request)
    return render(request, 'veterinaria/index.html',{'imagen':imagen})
    
    


def about(request):
    imagen = avatar(request)
    titulo = "Acerca de mi"
    contx = {
        'titulo' : titulo,
        'imagen':imagen
    }
    return render(request , 'veterinaria/about.html', contx)


@login_required
def empleados(request ):
    imagen = avatar(request)
    titulo = 'Empleados'
    empleados= Empleados.objects.all()
    if request.method == 'POST':
        formulario = EmpleadosFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            empleado= Empleados(data['nombre'],
            data['apellido'],
            data['dni'],
            data['telefono'],
            data['cargo'],
            data['email']
            )
        
            empleado.save()

            formulario = EmpleadosFormulario()
            contx = {
            'formulario':formulario,
            'empleados':empleados ,
            'imagen':imagen
            }
            return render(request, 'veterinaria/empleados.html', contx)
            
    else:
        formulario = EmpleadosFormulario()

        return render(request, 'veterinaria/empleados.html', {'titulo':titulo,'formulario':formulario,'empleados':empleados , 'imagen':imagen})

@login_required
def pacientes(request):
    imagen = avatar(request)
    titulo = 'Pacientes'
    pacientes= Pacientes.objects.all()
    if request.method == 'POST':
        formulario = PacientesFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            paciente= Pacientes(data['nombre'],data['apellido'],data['dni'],data['telefono'],data['nombre_mascota'],data['observacion'])
            
            paciente.save()

            formulario = PacientesFormulario()
            contx ={
                'titulo':titulo,
                'formulario':formulario,
                'pacientes':pacientes,
                'imagen':imagen
            }
            return render(request, 'veterinaria/pacientes.html', contx)

    else:
        formulario = PacientesFormulario()
        contx = {'titulo':titulo,
        'formulario':formulario,
        'pacientes':pacientes,
        'imagen':imagen
        }
        return render(request, 'veterinaria/pacientes.html', contx )
@login_required()
def productos(request):
    imagen = avatar(request)
    titulo = 'Productos'
    productos= Productos.objects.all()
    if request.method == 'POST':
        formulario = ProductosFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto= Productos(data['nombre'],data['precio'],data['stock'])
            
            producto.save()

            formulario = ProductosFormulario()
            contx ={
                'titulo':titulo,
                'formulario':formulario,
                'productos':productos,
                'imagen':imagen
            }
            return render(request, 'veterinaria/productos.html', contx)
    else:
        formulario = ProductosFormulario()
        contx = {
            'titulo':titulo,
            'formulario':formulario,
            'productos':productos,
            'imagen':imagen
        }
        return render(request, 'veterinaria/productos.html',contx)


@login_required
def contacto(request):
    imagen = avatar(request)
    titulo = 'Contacto'
    contactos = Contacto.objects.all()
    
    if request.method == "POST":
        formulario = ContactoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            contactos = Contacto(data['nombre'],data['apellido'],data['email'],data['telefono'],data['mensaje'])
            contactos.save()
            formulario = ContactoFormulario()
            contx = {
                'titulo':titulo,
                'formulario':formulario,
                'contactos':contactos,
                'imagen':imagen
            }
            return render(request, 'veterinaria/contacto.html', contx)
    else:
        formulario = ContactoFormulario()
        contx = {
            "titulo":titulo ,
            "formulario":formulario,
            'contactos':contactos,
            'imagen':imagen
            }
        return render(request, 'veterinaria/contacto.html',contx) 

@login_required()
def pages (request,):
    imagen = avatar(request)
    titulo : 'Paginas'
    contx = {
        'titulo':titulo,
        'imagen':imagen

    }
    return render(request, 'veterinaria/pages.html', contx)



# ======================================================================================================
# ======================================================================================================

@login_required()
def buscarEmpleado(request):
    imagen = avatar(request)
    data = request.GET.get('dni',"")                        #Tengo el get de la url
    error = ""
    print(data)         #chequeo la data que me llega
    error = ''
    if data:
        try:
            empleado = Empleados.objects.filter(dni=data)   #filtro al empleado por el dni
            # print(empleado)
            return render (request, 'veterinaria/buscar/buscarEmpleados.html', {'empleado':empleado[0], "id":data})   #renderizo y mando el empleado que tiene que ser [0] poruqe manda una lista
        except Exception as exc:
            print(exc)
            error = 'No se encontro el empleado'

    return render(request, 'veterinaria/buscar/buscarEmpleados.html', {'error':error})





@login_required()
def buscarPaciente(request):
    imagen = avatar(request)
    data = request.GET.get('nombre_mascota')                        #Tengo el get de la url
    error = ""
    print(data)         #chequeo la data que me llega
    error = ''
    if data:
        try:
            pacientes = Pacientes.objects.filter(nombre_mascota__icontains=data)   #filtro al empleado por el dni
            print(pacientes)
            return render (request, 'veterinaria/buscar/buscarPaciente.html', {'pacientes':pacientes[0], "id":data , 'imagen':imagen})   #renderizo y mando el empleado que tiene que ser [0] poruqe manda una lista
        except Exception as exc:
            print(exc)
            error = 'No se encontro el paciente'

    return render(request, 'veterinaria/buscar/BuscarPaciente.html', {'error':error , 'imagen':imagen})

@login_required()
def buscarProducto(request):
    imagen = avatar(request)
    data = request.GET.get('id')                        
    error = ""
    print(data)         #chequeo la data que me llega
    if data:
        try:
            producto = Productos.objects.filter(id__icontains=data)
            print(producto)
            return render (request, 'veterinaria/buscar/buscarProducto.html', {'producto':producto[0], "id":data ,'imagen':imagen})

        except Exception as exc:
            print(exc)
            error = 'No se encontro el producto'

    return render(request, 'veterinaria/buscar/buscarProducto.html', {'error':error , 'imagen':imagen})


# -----------------------------------------------------------------------------------------------------
# CRUD
# CREATE READ UPDATE DELETE



# ======================================================================================================

class EmpleadosList(ListView , LoginRequiredMixin):
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleados_list.html'
    context_object_name = 'empleados'
    titulo= 'Empleados trabajando'

class EmpleadosCreate(CreateView,LoginRequiredMixin):
    model = Empleados
   
    titulo= 'Crear empleado'
    success_url = "{% url 'empleados_lista' %}"
    fields = ['nombre', 'apellido', 'dni', 'telefono', 'cargo', 'email']



class EmpleadosUpdate(UpdateView,LoginRequiredMixin):      
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleados_form.html'
    success_url = "../../list"
    fields = ['nombre', 'apellido', 'dni', 'telefono', 'cargo', 'email']
    titulo= 'Actualizar empleado'

class EmpleadosDelete(DeleteView, LoginRequiredMixin):
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleadoconfirm_delete.html'
    success_url = "../../list"
    titulo = 'Eliminar empleado'

class EmpleadosDetail(DetailView, LoginRequiredMixin):
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleado_detalle.html'
    context_object_name = 'empleado'
    titulo= 'Detalle empleado'











class Pagina(LoginRequiredMixin,ListView):
    model = Page
    template_name = 'veterinaria/pages.html'
class PageCrear(LoginRequiredMixin,CreateView):
    model = Page
    success_url = "/pages"
    fields = ['titulo', 'contenido','slug']
class PageDetail(LoginRequiredMixin,DetailView):
    model = Page
    template_name = "veterinaria/page_detail.html"

class PageUpdate(LoginRequiredMixin,UpdateView):
    model = Page
    success_url = "/pages"
    fields = ['titulo', 'contenido','slug']

class PageDelete(LoginRequiredMixin,DeleteView):
    model = Page
    success_url = "/pages"

    # return render (request, 'veterinaria/pages.html', contexto)