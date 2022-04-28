from django.urls import path
from veterinaria.views import *
from usuario.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [


    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="veterinaria/logout.html"), name="logout"),
    path('registro/', register_request, name='register'),


    path("actualizar_perfil/", actualizar_usuario, name="EditarUsuario"),

    path("cargar_imagen/", cargar_imagen, name="CargarImagen")
]

  