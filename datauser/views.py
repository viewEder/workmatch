from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
# Vistas basadas en Clases:
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView

from registration.models import User
from .models import Academy, ProjectDev, Skills, Stack, EmploymentHistory, HobbiesExtras, Facts
from .forms import AcademyCreateForm

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django import forms

# Create your views here.
@method_decorator(login_required, name='dispatch')
<<<<<<< HEAD
class AcademyCreateView(CreateView):
    success_url = reverse_lazy('perfil-edit')
    template_name = 'datauser/academy_form.html'
    form_class = AcademyCreateForm

=======
class AcademyCreateView(CreateView, ListView):
    success_url = reverse_lazy('academy-create')
    template_name = 'datauser/academy_form.html'
    form_class = AcademyCreateForm
    model = Academy
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        return super().get_queryset().filter(user = self.request.user.id)
    
>>>>>>> 3e49c2810146763acfaf5a27b52d3e270546a905
class AcademyDetailView(DetailView):
    model = Academy

class AcamedyListView(ListView):
    model = Academy

class EmploymentHistoryListView(ListView):
    model = EmploymentHistory
