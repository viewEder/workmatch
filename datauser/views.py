from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
# Vistas basadas en Clases:
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView

from registration.models import User
from .models import Academy, ProjectDev, Skills, Stack, EmploymentHistory, HobbiesExtras, Facts
from .forms import AcademyCreateForm, SkillsCreateForm, HistoryCreateForm, ProjectCreateForm

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django import forms

# Create your views here.
@method_decorator(login_required, name='dispatch')
<<<<<<< HEAD
<<<<<<< HEAD
class AcademyCreateView(CreateView):
    success_url = reverse_lazy('perfil-edit')
    template_name = 'datauser/academy_form.html'
    form_class = AcademyCreateForm

=======
class AcademyCreateView(CreateView, ListView):
    success_url = reverse_lazy('perfil-edit')
    template_name = 'datauser/academy_form.html'
    form_class = AcademyCreateForm
    model = Academy
    
    def form_valid(self, form):
=======
class AcademyCreateView(CreateView, ListView):
    success_url = reverse_lazy('academy-create')
    template_name = 'datauser/academy_form.html'
    form_class = AcademyCreateForm
    model = Academy
    
    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
>>>>>>> 35d0a57598cb14328213487a6dd9fea33da2f79f
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
<<<<<<< HEAD
        return super().get_queryset().filter(user = self.request.user.id)
    
>>>>>>> 3e49c2810146763acfaf5a27b52d3e270546a905
=======
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset().filter(user = self.request.user.id)
    
>>>>>>> 35d0a57598cb14328213487a6dd9fea33da2f79f
class AcademyDetailView(DetailView):
    model = Academy

class AcamedyListView(ListView):
    model = Academy

class EmploymentHistoryListView(ListView):
    model = EmploymentHistory
<<<<<<< HEAD
=======

@method_decorator(login_required, name='dispatch')
class SkillsCreateView(CreateView):
    success_url = reverse_lazy('perfil-edit')
    template_name = 'datauser/skills_form.html'
    form_class = SkillsCreateForm

@method_decorator(login_required, name='dispatch')
class HistoryCreateView(CreateView):
    success_url = reverse_lazy('perfil-edit')
    template_name = 'datauser/history_form.html'
    form_class = HistoryCreateForm

class ProjectCreateView(CreateView):
    success_url = reverse_lazy('perfil-edit')
    template_name = 'datauser/project_form.html'
    form_class =ProjectCreateForm
>>>>>>> 35d0a57598cb14328213487a6dd9fea33da2f79f
