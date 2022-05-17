
from django.conf import settings
from django.shortcuts import redirect, render
from django.conf import settings
from django.core.mail import send_mail
from .forms import PersonaForm
from .models import Persona

def inicio(request):
    personas = Persona.objects.all()
    contexto = {
        'personas':personas
    }
    return render(request, 'index.html',contexto)

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
            return redirect('index')
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
            return redirect('index')
   return render(request, 'crear_persona.html', contexto)

def eliminarPersona(request, id):
    persona = Persona.objects.get(idpersona = id)
    persona.delete()
    return redirect('index')