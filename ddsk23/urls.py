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
from django.contrib import admin
from django.urls import path
from principal.views import crearPersona, editarPersona, eliminarPersona, formularioContacto, inicio, contactar
from principal.class_view import PersonaCreate, PersonaDelete, PersonaList, PersonaUpdate


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PersonaList.as_view(),name= 'index'),
    
    path('formularioContacto/', formularioContacto),
    path('contactar/', contactar),
    path('crear_persona/', PersonaCreate.as_view(), name = 'crear_persona'),
    path('editar_persona/<int:pk>/' , PersonaUpdate.as_view(), name = 'editar_persona'),
    path('eliminar_persona/<int:pk>/', PersonaDelete.as_view(), name = 'eliminar_persona'),
    
]

""" path('',inicio,name= 'index'), """
""" path('eliminar_persona/<int:id>/' ,eliminarPersona, name = 'eliminar_persona'), """