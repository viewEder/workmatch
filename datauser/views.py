from typing import Any
from django.db import models
from django.shortcuts import render, get_object_or_404
# Vistas basadas en Clases:
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, CreateView

from registration.models import User
from .models import Academy, ProjectDev, Skills, Stack, EmploymentHistory, HobbiesExtras, Facts
from .forms import AcademyCreateForm, SkillsCreateForm, HistoryCreateForm, ProjectCreateForm, StackCreateForm, FactsCreateForm

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from django.urls import reverse_lazy
from django import forms

import requests
from datetime import datetime 

# Create your views here.
@method_decorator(login_required, name='dispatch')
class AcademyCreateView(CreateView, ListView):
    success_url = reverse_lazy('academy-create')
    template_name = 'datauser/academy_form.html'
    form_class = AcademyCreateForm
    model = Academy
    
    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset().filter(user = self.request.user.id)
    
class AcademyDetailView(DetailView):
    model = Academy

class AcamedyListView(ListView):
    model = Academy

class EmploymentHistoryListView(ListView):
    model = EmploymentHistory

@method_decorator(login_required, name='dispatch')
class SkillsCreateView(CreateView, ListView):
    success_url = reverse_lazy('skills-create')
    template_name = 'datauser/skills_form.html'
    form_class = SkillsCreateForm
    model = Skills

    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset().filter(user = self.request.user.id)

@method_decorator(login_required, name='dispatch')
class HistoryCreateView(CreateView, ListView):
    success_url = reverse_lazy('history-create')
    template_name = 'datauser/history_form.html'
    form_class = HistoryCreateForm
    model = EmploymentHistory

    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset().filter(user = self.request.user.id)
    
@method_decorator(login_required, name='dispatch')
class ProjectCreateView(CreateView, ListView):
    success_url = reverse_lazy('project-create')
    template_name = 'datauser/project_form.html'
    form_class =ProjectCreateForm
    model = ProjectDev

    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
        form.instance.user = self.request.user
        return super().form_valid(form)
    
    def get_queryset(self):
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset().filter(user = self.request.user.id)

@method_decorator(login_required, name='dispatch')
class StackCreateView(CreateView, ListView):
    success_url = reverse_lazy('stack-create')
    template_name = 'datauser/stack_form.html'
    form_class = StackCreateForm
    model = Stack

    def get_queryset(self):
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset()

@method_decorator(login_required, name='dispatch')
class FactsCreateView(CreateView, ListView):
    success_url = reverse_lazy('fact-create')
    template_name = 'datauser/facts_form.html'
    form_class = FactsCreateForm
    model = Facts

    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset().filter(user = self.request.user.id)


def get_job_data(request):
    api_url = "https://www.arbeitnow.com/api/job-board-api"

    try:
        response = requests.get(api_url)

        if response.status_code == 200:
            data = response.json().get('data', [])
            for job in data:
                job['created_at'] = datetime.fromtimestamp(job['created_at'])
            return render(request, 'job_data.html', {'api_data': data})
        else:
            return render(request, 'job_data.html', {'error_message': 'API request failed'})

    except requests.exceptions.RequestException as e:
        return render(request, 'job_data.html', {'error_message': 'API request error'})