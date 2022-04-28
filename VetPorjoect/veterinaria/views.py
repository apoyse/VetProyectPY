
from django.shortcuts import redirect, render, HttpResponse
from django.shortcuts import render
from veterinaria.models import *
from veterinaria.fomrs import *

#Vistas Basasadas en clase
from django.views.generic import ListView #clase basada en vistas
from django.views.generic import DetailView, DeleteView, UpdateView, CreateView


#User Login
from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import login , authenticate 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


from usuario.views import *





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
@login_required()
def borrar_empleado(request,dni_id):
    try:
        empleado = Empleados.objects.get(dni=dni_id)
        empleado.delete()
    except Exception as exc:
        return render (request, 'veterinaria/empleados.html')
    
    return render (request, 'veterinaria/empleados.html')

@login_required()
def update_empleado(request,dni_id):
        empleado = Empleados.objects.get(dni=dni_id)   
        if request.method == 'post':
            formulario = EmpleadosFormulario(request.POST)
            if formulario.is_valid():
                informacion = formulario.cleaned_data
                empleado.nombre = informacion['nombre']
                empleado.apellido = informacion['apellido']
                empleado.dni = informacion['dni']
                empleado.telefono = informacion['telefono']
                empleado.email = informacion['email']
                empleado.save()
        else:
            
                empleado = Empleados.objects.get(dni=dni_id)

                formulario= EmpleadosFormulario(initial={"nombre":empleado.nombre,"apellido":empleado.apellido,"dni":empleado.dni,"telefono":empleado.telefono,"cargo":empleado.cargo,"email":empleado.email})
                return render(request, 'veterinaria/update_empleado.html', {'formulario':formulario})

        return render(request, 'veterinaria/update_empleado.html', {'formulario':formulario })




# ======================================================================================================

class EmpleadosList(ListView , LoginRequiredMixin):
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleados_list.html'
    context_object_name = 'empleados'


class EmpleadosCreate(CreateView,LoginRequiredMixin):
    model = Empleados
   
    
    success_url = "{% url 'empleados_lista' %}"
    fields = ['nombre', 'apellido', 'dni', 'telefono', 'cargo', 'email']



class EmpleadosUpdate(UpdateView,LoginRequiredMixin):      
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleados_form.html'
    success_url = "../../list"
    fields = ['nombre', 'apellido', 'dni', 'telefono', 'cargo', 'email']
  

class EmpleadosDelete(DeleteView, LoginRequiredMixin):
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleadoconfirm_delete.html'
    success_url = "../../list"


class EmpleadosDetail(DetailView, LoginRequiredMixin):
    model = Empleados
    template_name = 'veterinaria/empleados_funciones/empleado_detalle.html'
    context_object_name = 'empleado'
 








# def login_request(request):
    
#     if request.method == 'POST':
#         form = AuthenticationForm(request, data = request.POST)
#         if form.is_valid():
#             usuario = form.cleaned_data.get('username')
#             contra = form.cleaned_data.get('password')


#             user = authenticate(username = usuario, password = contra)

#             if user is not None:
#                 login(request, user)
#                 imagen= avatar(request)
#                 # dict_ctx = {'title':'inicio' , 'page': usuario}
#                 return render (request, 'veterinaria/index.html' , {'mensaje':f'Bienvenido {usuario}', 'imagen': imagen})

#             else:
#                 return render(request,'veterinaria/index.html' , {'mensaje':'Usuario o contraseña incorrectos'})
#         else:
#             dict_ctx = {
#             'title':'inicio',
#             'page': 'anonymous',
#             'errors': 'Revise los datos'
#              }
#             return render(request, 'veterinaria/index.html', dict_ctx)  

        #     if user is not None:
        #         login(request, user)
        #         imagen= avatar(request)
        #         # dict_ctx = {'title':'inicio' , 'page': usuario}
        #         return render (request, 'veterinaria/index.html' , {'mensaje':f'Bienvenido {usuario}', 'imagen': imagen})

        #     else:
        #         return render(request,'veterinaria/index.html' , {'mensaje':'Usuario o contraseña incorrectos'})
        # else:
        #     dict_ctx = {
        #     'title':'inicio',
        #     'page': 'anonymous',
        #     'errors': 'Revise los datos'
        #      }
        #     return render(request, 'veterinaria/index.html', dict_ctx)  

    
   
#     form = AuthenticationForm()
#     return render(request, 'veterinaria/login.html', {'form':form})



# def register_request(request):
   
#     if request.method == 'POST':

#         form = UserRegisterForm(request.POST)

#         if form.is_valid():
#             username = form.cleaned_data['username']
#             form.save()


#             return redirect('index')
#         else:
#             dict_ctx = {
#                 "title": "Inicio",
#                 "page": "anonymous",
#                 "errors": ["No paso las validaciones"] 
#                 }
#             return render(request, "veterinaria/index.html", dict_ctx)
#     else:
#         form = UserRegisterForm()

    #         return redirect('index')
    #     else:
    #         dict_ctx = {
    #             "title": "Inicio",
    #             "page": "anonymous",
    #             "errors": ["No paso las validaciones"] 
    #             }
    #         return render(request, "veterinaria/index.html", dict_ctx)
    # else:
    #     form = UserRegisterForm()

    
#     return render(request, 'veterinaria/registro.html', { 'form':form})





# @login_required()
# def actualizar_usuario(request):
#     imagen = avatar(request)
#     titulo = "Actualizar Usuario"
#     usuario = request.user

#     if request.method == "POST":
#         formulario = UsuarioEditForm(request.POST)

#         if formulario.is_valid():
#             data = formulario.cleaned_data

#             usuario.email = data["email"]
#             usuario.password1 = data["password1"]
#             usuario.password2 = data["password2"]
#             usuario.last_name = data["last_name"]
#             usuario.first_name = data["first_name"]

#             usuario.save()


#             return redirect("Inicio")
#         else:
#             formulario = UsuarioEditForm(initial={"email": usuario.email})  
#             contx = {
#                 "form": formulario,
#                 "errors": ["Datos invalidos"] ,
#                 'imagen': imagen,
#                 'titulo': titulo
#             }
#             return render(request,  "veterinaria/editar_usuario.html",contx )

        #     return redirect("Inicio")
        # else:
        #     formulario = UsuarioEditForm(initial={"email": usuario.email})  
        #     contx = {
        #         "form": formulario,
        #         "errors": ["Datos invalidos"] ,
        #         'imagen': imagen,
        #         'titulo': titulo
        #     }
        #     return render(request,  "veterinaria/editar_usuario.html",contx )


#     else:
#         formulario = UsuarioEditForm(initial={"email": usuario.email})  
#         return render(request,  "veterinaria/editar_usuario.html", {"form": formulario , 'imagen': imagen, 'titulo': titulo})


# @login_required()
# def cargar_imagen(request):

#     if request.method == "POST":

#         formulario = AvatarFormulario(request.POST,request.FILES)

#         if formulario.is_valid():

#             usuario = request.user

#             avatar = Avatar.objects.filter(user=usuario)

#             if len(avatar) > 0:
#                 avatar = avatar[0]
#                 avatar.imagen = formulario.cleaned_data["imagen"]
#                 avatar.save()

#             else:
#                 avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
#                 avatar.save()
            
#         return redirect("index")
#     else:

#         formulario = AvatarFormulario()
#         return render(request, "veterinaria/cargar_imagen.html", {"form": formulario})




# def avatar(request):

#     if request.user.username:
#         avatar = Avatar.objects.filter(user = request.user)
#         if len(avatar) > 0:
#             imagen = avatar[0].imagen.url
            
#         else:
#             imagen = '/media/avatar/predeterminada.png'
#     else:
#         imagen = '/media/avatar/predeterminada.png'
#     return (imagen)




class Pagina(ListView):

    def get(self,request,*args,**kwargs):
        pages = list(Page.objects.all().values_list('id', flat=True))

        contexto = { 
        'pages': pages
    }

       

        return render(request,'pages.html',contexto)