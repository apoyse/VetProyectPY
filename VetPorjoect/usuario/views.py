from django.shortcuts import render , redirect


from django.contrib.auth.forms import AuthenticationForm ,UserCreationForm
from django.contrib.auth import login , authenticate 
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from usuario.models import *
from usuario.forms import *

def login_request(request):

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')


            user = authenticate(username = usuario, password = contra)

            if user is not None:
                login(request, user)
                imagen= avatar(request)
                # dict_ctx = {'title':'inicio' , 'page': usuario}
                return render (request, 'veterinaria/index.html' , {'mensaje':f'Bienvenido {usuario}', 'imagen': imagen})

            else:
                return render(request,'veterinaria/index.html' , {'mensaje':'Usuario o contraseña incorrectos'})
        else:
            dict_ctx = {
            'title':'inicio',
            'page': 'anonymous',
            'errors': 'Revise los datos'
             }
            return render(request, 'veterinaria/index.html', dict_ctx)  
    
   
    form = AuthenticationForm()
    return render(request, 'veterinaria/login.html', {'form':form})



def register_request(request):
   
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()

            return redirect('index')
        else:
            dict_ctx = {
                "title": "Inicio",
                "page": "anonymous",
                "errors": ["No paso las validaciones"] 
                }
            return render(request, "veterinaria/index.html", dict_ctx)
    else:
        form = UserRegisterForm()
    
    return render(request, 'veterinaria/registro.html', { 'form':form})





@login_required()
def actualizar_usuario(request):
    imagen = avatar(request)
    titulo = "Actualizar Usuario"
    usuario = request.user

    if request.method == "POST":
        formulario = UsuarioEditForm(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data

            usuario.email = data["email"]
            usuario.password1 = data["password1"]
            usuario.password2 = data["password2"]
            usuario.last_name = data["last_name"]
            usuario.first_name = data["first_name"]

            usuario.save()

            return redirect("Inicio")
        else:
            formulario = UsuarioEditForm(initial={"email": usuario.email})  
            contx = {
                "form": formulario,
                "errors": ["Datos invalidos"] ,
                'imagen': imagen,
                'titulo': titulo
            }
            return render(request,  "veterinaria/editar_usuario.html",contx )

    else:
        formulario = UsuarioEditForm(initial={"email": usuario.email})  
        return render(request,  "veterinaria/editar_usuario.html", {"form": formulario , 'imagen': imagen, 'titulo': titulo})


@login_required()
def cargar_imagen(request):

    if request.method == "POST":

        formulario = AvatarFormulario(request.POST,request.FILES)

        if formulario.is_valid():

            usuario = request.user

            avatar = Avatar.objects.filter(user=usuario)

            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.imagen = formulario.cleaned_data["imagen"]
                avatar.save()

            else:
                avatar = Avatar(user=usuario, imagen=formulario.cleaned_data["imagen"])
                avatar.save()
            
        return redirect("index")
    else:

        formulario = AvatarFormulario()
        return render(request, "veterinaria/cargar_imagen.html", {"form": formulario})




def avatar(request):

    if request.user.username:
        avatar = Avatar.objects.filter(user = request.user)
        if len(avatar) > 0:
            imagen = avatar[0].imagen.url
            
        else:
            imagen = '/media/avatar/predeterminada.png'
    else:
        imagen = '/media/avatar/predeterminada.png'
    return (imagen)


# Create your views here.
