from django.urls import path
from veterinaria.views import *
from usuario.views import *
from django.contrib.auth.views import LogoutView



urlpatterns = [


    path('login/', login_request, name='login'),
    path('logout/', LogoutView.as_view(template_name="user/logout.html"), name="logout"),
    path('registro/', register_request, name='register'),
    path('profile/<username>/', get_user_profile, name='profile'),

    
    path("actualizar_perfil/", actualizar_usuario, name="EditarUsuario"),

    path("cargar_imagen/", cargar_imagen, name="CargarImagen"),
    path("cambiar_imagen/", cargar_imagen2 , name="CargarImagen2")
]

  