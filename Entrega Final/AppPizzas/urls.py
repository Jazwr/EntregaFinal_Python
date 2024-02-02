from django.urls import path
from AppPizzas.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.conf.urls import include

urlpatterns = [

    #URL de inicio
    path('',inicio, name="Inicio"),
    #path('admin',admin.site.urls),

    #URL sobre mi
    path('sobremi/',sobremi,name="sobremi"),

    #URL's de registro
    path('login/',inicioSesion, name="Login"),
    path('registro/',registro, name="Registro"),
    path('edit/',editar_usuario,name="Editar Usuario"),
    path('logout/',cerrarSesion,name="Logout"),


    
    #URL's creación y búsqueda
    path('crearnuevaPizza/',agregarPizza, name="Crear Pizza"),   
    path('asesor/',agregar_asesor,name="Asesores"),
    path('Pizzas/', busquedaPizza, name="Buscar Pizzas"),
    path('resultados/', resultados,name='resultadosBusq'),



    #CRUD de Pizzas usando Clases
    path('Pizza/list/', ListaPizza.as_view(),name='PizzaLeer'),
    path('Pizza/<int:pk>', DetallePizza.as_view(),name='PizzaDetalle'),
    path('Pizza/crear/', CrearPizza.as_view(),name='PizzaCrear'),
    path('Pizza/editar/<int:pk>', ActualizarPizza.as_view(),name='PizzaEditar'),
    path('Pizza/borrar/<int:pk>', BorrarPizza.as_view(),name='PizzaBorrar'),

    #CRUD de Creadores usando Clases
    path('Creador/list/', ListaCreador.as_view(),name='CreadorLeer'),
    path('Creador/<int:pk>', DetalleCreador.as_view(),name='CreadorDetalle'),
    path('Creador/crear/', CrearCreador.as_view(),name='CreadorCrear'),
    path('Creador/editar/<int:pk>', ActualizarCreador.as_view(),name='CreadorEditar'),
    path('Creador/borrar/<int:pk>', BorrarCreador.as_view(),name='CreadorBorrar'),

    #CRUD de Asesores usando Clases
    path('Asesor/list/', ListaAsesor.as_view(),name='AsesorLeer'),
    path('Asesor/<int:pk>', DetalleAsesor.as_view(),name='AsesorDetalle'),
    path('Asesor/crear/', CrearAsesor.as_view(),name='AsesorCrear'),
    path('Asesor/editar/<int:pk>', ActualizarAsesor.as_view(),name='AsesorEditar'),
    path('Asesor/borrar/<int:pk>', BorrarAsesor.as_view(),name='AsesorBorrar'),
]

urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
