from django.urls import path
from veterinaria.views import *



urlpatterns = [
    path('', index, name='index'),
    
    path('pacientes/', pacientes, name='pacientes'),
   
    path('productos/', productos, name='productos'),
    path('empleados/', empleados, name='empleados'),
    path('contacto/', contacto, name='contacto'),
    path('about/', about, name='about'),
    path('buscarPaciente/', buscarPaciente, name='buscarPaciente'),
   
    path('buscarProducto/', buscarProducto, name='buscarProducto'),
    path('buscarEmpleado/', buscarEmpleado, name='buscarEmpleado'),

    path('empleados/<dni_id>/update', update_empleado, name='update_empleado'),
    path('empleados/<dni_id>/delete', borrar_empleado, name='borrar_empleado'),



    path ('empleados/list/' ,EmpleadosList.as_view(),name = 'empleados_list'),
    path('empleados/create/', EmpleadosCreate.as_view(), name='empleados_create'),
    path('empleados/update/<pk>/', EmpleadosUpdate.as_view(), name='empleados_update'),
    path('empleados/delete/<pk>/', EmpleadosDelete.as_view(), name='empleados_delete'),
    path('empleados/<pk>/' ,EmpleadosDetail.as_view(), name='empleados_detail'),

    path('pages/', pages, name='pages'),

    path('login', login, name='login'),
]
   