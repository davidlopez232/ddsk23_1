"""ddsk23 URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from re import template
from django.contrib import admin
from django.urls import path
from principal.views import ListadoTipoPersona, TipoPersonaDetalle, TipoPersonaCrear, TipoPersonaActualizar, TipoPersonaEliminar, crearPersona, editarPersona, eliminarPersona, formularioContacto, indextemplate, inicio, contactar
from principal.class_view import PersonaCreate, PersonaDelete, PersonaList, PersonaUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('formulario/',formularioContacto ),
    path('contactar/',contactar ),
    path('index/', ListadoTipoPersona.as_view(template_name ="index.html"), name='leer'),
    
 
    # La ruta 'detalles' en donde mostraremos una página con los detalles deun Categoria o registro
    path('detalle/<int:pk>',TipoPersonaDetalle.as_view(template_name = "detalle.html"),name='detalles'),
 
    # La ruta 'crear' en donde mostraremos un formulario para crear un nuevoCategoria o registro  
    path('crear', TipoPersonaCrear.as_view(template_name ="crear.html"), name='crear'),
 
    # La ruta 'actualizar' en donde mostraremos un formulario paraactualizar un categoriao registro de la Base de Datos
    path('editar/<int:pk>',TipoPersonaActualizar.as_view(template_name = "actualizar.html"),name='actualizar'),
 
    # La ruta 'eliminar' que usaremos para eliminar un Categoria o registrode la Base de Datos
    path('eliminar/<int:pk>', TipoPersonaEliminar.as_view(),name='eliminar.html'),    
]

""" urlpatterns = [
    path('admin/', admin.site.urls),
    path('index1',PersonaList.as_view(),name= 'index1'),
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar), 
    path('index', indextemplate),
]
urlpatterns = [
    path('index/', ListadoTipoPersona.as_view(template_name = "index.html"), name='leer'),
    
    path('detalle/<int:pk>', TipoPersonaDetalle.as_view(template_name = "detalle.html"), name='detalle'),
  
    path('crear/', TipoPersonaCrear.as_view(template_name = "crear.html"), name='crear'),

    path('editar/<int:pk>', TipoPersonaActualizar.as_view(template_name = "actualizar.html "), name='actualizar'),

    path('eliminar/', TipoPersonaEliminar.as_view(), name='eliminar'),
    
] """

""" path('',inicio,name= 'index'), """
""" path('eliminar_persona/<int:id>/' ,eliminarPersona, name = 'eliminar_persona'), """


""" path('crear_persona/', PersonaCreate.as_view(), name = 'crear_persona'),
    path('editar_persona/<int:pk>/' , PersonaUpdate.as_view(), name = 'editar_persona'),
    path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(), name = 'eliminar_persona'), """
    