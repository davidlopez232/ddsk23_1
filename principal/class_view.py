from django import dispatch, http
import django
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.urls import reverse_lazy
from .forms import PersonaForm
from .models import Persona


"""

class ListView(View):
    dispatch : verificar el metodo de la solicitud http
    http_not_allowed

    def dispatch()

    model = Persona
    template_name = 'index.html'

    def get_context_data(self):
        context = {}
        context['queryset'] = self.get_queryset()

    def get_queryset(self):
        return self.model.objects.all()

    def get(self,request,*args,**kwargs): // para listview

    def get_templates_names():
        return self.template_name



    def post(self,request,*args,**kwargs): // para create,delete,update view
"""

class PersonaList(ListView):
    model = Persona
    template_name = 'index.html'

    def get_queryset(self):
        return self.model.objects.all()[:3]

class PersonaCreate(CreateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaUpdate(UpdateView):
    model = Persona
    form_class = PersonaForm
    template_name = 'crear_persona.html'
    success_url = reverse_lazy('index')

class PersonaDelete(DeleteView):
    model = Persona
    template_name = 'verificacion.html'
    success_url = reverse_lazy('index')