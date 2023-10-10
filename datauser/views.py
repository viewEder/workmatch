from django.shortcuts import render
# Vistas basadas en Clases:
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView

from .models import Academy, ProjectDev, Skills, Stack, EmploymentHistory, HobbiesExtras, Facts
from .forms import AcademyCreateForm

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django import forms

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AcademyCreateView(CreateView):
    success_url = reverse_lazy('perfil-edit')
    template_name = 'datauser/academy_form.html'
    form_class = AcademyCreateForm

class AcademyDetailView(DetailView):
    model = Academy

class AcamedyListView(ListView):
    model = Academy

class EmploymentHistoryListView(ListView):
    model = EmploymentHistory
