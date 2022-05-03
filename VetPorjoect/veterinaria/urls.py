from django.urls import path , include
from veterinaria.views import *
from django.contrib.auth.views import LogoutView
from usuario.views import *
from usuario.urls import *


urlpatterns = [
    path('', index, name='index'),
    
    path('pacientes/', pacientes, name='pacientes'),
   
    path('productos/', productos, name='productos'),
    path('empleados/', empleados, name='empleados'),
    path('contacto/', contacto, name='contacto'),
    path('about/', about, name='about'),

    path('veterinaria/buscarPaciente/', buscarPaciente, name='buscarPaciente'),
    path('veterinaria/buscarProducto/', buscarProducto, name='buscarProducto'),
    path('veterinaria/buscarEmpleado/', buscarEmpleado, name='buscarEmpleado'),

    # path('empleados/<dni_id>/update', update_empleado, name='update_empleado'),
    # path('empleados/<dni_id>/delete', borrar_empleado, name='borrar_empleado'),



    path ('empleados/list/' ,EmpleadosList.as_view(),name = 'empleados_list'),
    path('empleados/create/', EmpleadosCreate.as_view(), name='empleados_create'),
    path('empleados/update/<pk>/', EmpleadosUpdate.as_view(), name='empleados_update'),
    path('empleados/delete/<pk>/', EmpleadosDelete.as_view(), name='empleados_delete'),
    path('empleados/<pk>/' ,EmpleadosDetail.as_view(), name='empleados_detail'),

    path('pages/', Pagina.as_view(), name='pages'),
    path('pages/create/', PageCrear.as_view(), name='page_create'),
    path("pages/<pk>/", PageDetail.as_view(), name="page_detail"),
    path("pages/editar/<pk>/", PageUpdate.as_view(), name="page_update"),
    path("pages/borrar/<pk>/", PageDelete.as_view(), name="page_delete"),
    path('notemplate/' , no_template, name='notemplate'),

    path('posts/',Postview.as_view(),name='posts'),
    path('post/<int:pk>',ListarPosts.as_view(),name='post_detalle'),
    path('creaPost/',CrearPosts.as_view(),name='crear_post'),
    path('post/mod/<int:pk>/',EditPost.as_view(),name='edit_post'),
    path('post/<int:pk>/borrar',BorrarPost.as_view(),name='delete_post'),
    path('post/<int:pk>/comentaPost/',CrearComentario.as_view(),name='comenta_post'),
    # path('like/<int:pk>',LikeView,name='like-post'),
    path('account/', include('usuario.urls')),

    path('messages/', include('direct.urls')),


]
   