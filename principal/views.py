
from django.conf import settings
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.conf import settings
from django.core.mail import send_mail
from .forms import PersonaForm
from .models import Persona
from .models import *
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms

def inicio(request):
    personas = Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request, 'index1.html',contexto)

def formularioContacto(request):
    return render(request, 'formularioContacto.html')

def contactar(request):
    if request.method == "POST":
        asunto = request.POST ["txtAsunto"]
        mensaje = request.POST ["txtMensaje"] + " / Email: " + request.POST["txtEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["kasekage233@gmail.com"]
        send_mail(asunto, mensaje, email_desde, email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioContato.html")

def crearPersona(request):
    if request.method == 'GET':
        form = PersonaForm()
        contexto = {
            'form':form
       }
    else:
        form = PersonaForm(request.POST)
        contexto = {
            'form':form
       }
        if form.is_valid():
            form.save()
            return redirect('index1')
    return render(request, 'crear_persona.html', contexto)

def editarPersona(request, id):
   persona = Persona.objects.get(idpersona = id)
   if request.method == 'GET':
       form = PersonaForm(instance = persona) 
       contexto = {
           'form':form
       }
   else:  
        form = PersonaForm(request.POST, instance = persona)
        contexto = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('index1')
   return render(request, 'crear_persona.html', contexto)

def eliminarPersona(request, id):
    persona = Persona.objects.get(idpersona = id)
    persona.delete()
    return redirect('index1')

def indextemplate(request):
    return render(request, 'inicio.html')


class ListadoTipoPersona(ListView):
    model = TipoPersona
   
class TipoPersonaCrear(SuccessMessageMixin, CreateView):
    model =TipoPersona
    form = TipoPersona
    fields = '__all__'
    success_message ='TipoPersona creado correctamente'
     
    def get_success_url(self):        
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TipoPersonaDetalle (DetailView):
    model =TipoPersona
class  TipoPersonaActualizar(SuccessMessageMixin,UpdateView):
    model =  TipoPersona
    form = TipoPersona
    fields = "__all__" # Le decimos a Django que muestre todos los campos de la tabla 'postres' de nuestra Base de Datos
    success_message = 'tipo_persona Actualizado Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
    def get_success_url(self):              
        return reverse('leer') # Redireccionamos a la vista principal 'leer'
class TipoPersonaEliminar(SuccessMessageMixin, DeleteView):
    model = TipoPersona
    form = TipoPersona
    fields = "__all__"    
 
    # Redireccionamos a la página principal luego de eliminar un registro o postre
    def get_success_url(self):

        success_message = 'tipoPersona Eliminada Correctamente !' # Mostramos este Mensaje luego de Editar un Postre
        messages.success (self.request, (success_message))      
        return reverse('leer') # Redireccionamos a la vista principal 'leer'