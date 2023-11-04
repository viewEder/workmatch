from typing import Optional, Type
from django.forms.models import BaseModelForm
from django.shortcuts import render

# vistas basadas en clases:
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView

# Método decorador de login:
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import User, Links, Excerp
from datauser.models import Academy, ProjectDev, Skills, EmploymentHistory, HobbiesExtras, Facts

# Formularios propios:
from .forms import SingUpUserFormWithEmail, ProfileUserForm, ExcerpCreateForm

from django.urls import reverse_lazy
from django import forms
from django.http import HttpResponseRedirect
from core.util import get_edad

# Create your views here.
@method_decorator(login_required, name='dispatch')
class ProfileUserView(TemplateView):
    # Template:
    template_name = 'registration/profile.html'  
    links_list = []
    excerp_list = []
    hobbies_list = []
    academy_list = []
    project_list = []
    skill_list = []
    employment_list = []
    facts_list = []
    age_user = 0

    def get(self, request, *args, **kwargs): 
        links_user = Links.objects.filter(user = request.user.id)
        excerp_user = Excerp.objects.filter(user = request.user.id)
        hobbies_user = HobbiesExtras.objects.filter(user = request.user.id)
        academy_users = Academy.objects.filter(user = request.user.id)
        project_user = ProjectDev.objects.filter(user = request.user.id)
        skills_user = Skills.objects.filter(user = request.user.id)
        employment_user = EmploymentHistory.objects.filter(user = request.user.id)
        facts_user = Facts.objects.filter(user = request.user.id)

        # Para calcular la fecha de nacimiento:
        user = request.user
        fechanace = user.birthday
        self.age_user = get_edad(fechanace)
        
        # Enlaces (links):
        for item in links_user:
            link = {
                'type_link': item.type_link,
                'link': item.link
            }
            if link not in self.links_list:
                 self.links_list.append(link)
        
        # Resumen (excerps):
        for item in excerp_user:
            excerp = {
                'excerption_type': item.excerption_type,
                'content': item.content
            }

            if excerp not in self.excerp_list:
                self.excerp_list.append(excerp)

        # Hobbies de usuario:
        for hobbies in hobbies_user:
            if hobbies.hobby not in self.hobbies_list:
                self.hobbies_list.append(hobbies.hobby)

        # Por Estudios realizados
        for item in academy_users:
            academy = {
                    'id': item.id,
                    'type_degree' : item.type_degree,
                    'academy_name' : item.academy_name,
                    'degree_obtained' : item.degree_obtained,
                    'degree_esp': item.degree_esp,
                    'start_date' : item.start_date,
                    'finish_date' : item.finish_date,
                    'in_progress' : item.in_progress
                }
            
            if academy not in self.academy_list:
                self.academy_list.append(academy)
        
        # Por Proyectos en los que participó:
        for item in project_user:
            project = {
                'id': item.id,
                'stack': item.stack,
                'name_project': item.name_project,
                'resume_project': item.resume_project,
                'url_repo': item.url_repo,
                'year_production': item.year_production,
                'developing': item.developing
            }

            if project not in self.project_list:
                self.project_list.append(project)

        # Por Habilidades de usuario:
        for item in skills_user:
            # Cambiamos el valor de texto a numérico:
            if item.level == 'Basico':
                item.level = 25
            if item.level == 'Intermedio':
                item.level = 50
            if item.level == 'Alto':
                item.level = 75
            if item.level == 'Avanzado':
                item.level = 100
            # Agregamos el skill al diccionario: 
            skill = {
                'id': item.id,
                'skill': item.skill,
                'level': item.level,
                'description': item.description,
            }

            if skill not in self.skill_list:
                self.skill_list.append(skill)

        # Por Empleos de usuario:
        for item in employment_user:
            employment = {
                'id': item.id,
                'stack': item.stack,
                'company': item.company,
                'position': item.position,
                'job_description': item.job_description,
                'start_date': item.start_date,
                'end_date': item.end_date,
                'still_work': item.still_work
            }

            if employment not in self.employment_list:
                self.employment_list.append(employment)

        # Por Hechos de usuario:
        for item in facts_user:
            fact = {
                'id': item.id,
                'fact': item.fact,
                'value': item.value,
            }

            if fact not in self.facts_list:
                self.facts_list.append(fact)


        # Retornamos todos los valores obtenidos en el diccionario de contexto:
        return render(request, self.template_name, context = { 'links': self.links_list,
                                                               'excerp': self.excerp_list, 
                                                               'academia': self.academy_list,
                                                               'proyectos': self.project_list,
                                                               'habilidades': self.skill_list,
                                                               'empleos': self.employment_list,
                                                               'hechos': self.facts_list,
                                                               'hobbies': self.hobbies_list,
                                                               'edad': self.age_user
                                                             })

class SignUpUserView(CreateView):
    form_class= SingUpUserFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'   

    def get_form(self, form_class= None):
        form = super(SignUpUserView, self).get_form()
        # Agregamos estilos al formulario a través de widgets:
        form.fields['username'].widget = forms.TextInput(attrs={'placeholder':'NickName', 'class':'form-control mb-2'})
        form.fields['email'].widget = forms.EmailInput(attrs={'placeholder':'email@mail.com', 'class':'form-control mb-2'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Password'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'Confirma el Password'})

        return form
    

@method_decorator(login_required, name='dispatch')
class ProfileUserUpdate(UpdateView):
    form_class = ProfileUserForm
    success_url = reverse_lazy('perfil')
    template_name = 'registration/profile_form.html'

    # Métodos:
    def get_object(self):
        profile, created = User.objects.get_or_create(id = self.request.user.id) # QuerySet de usuario: Select * from user where id = request.user.id
        return profile


@method_decorator(login_required, name='dispatch')
class ExcerpCreateView(CreateView, ListView):
    success_url = reverse_lazy('excerp-create')
    template_name = 'registration/excerp_form.html'
    form_class = ExcerpCreateForm
    model = Excerp

    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
        form.instance.user = self.request.user
        return super().form_valid(form)

    def get_queryset(self):
        """ Método para filtrar los datos del usuario que se encuentra logueado """
        return super().get_queryset().filter(user = self.request.user.id)

@method_decorator(login_required, name='dispatch')
class ExcerpUpdateView(UpdateView):
    success_url = reverse_lazy('excerp-create')
    template_name = 'registration/excerp_upd_form.html'
    form_class = ExcerpCreateForm

    # Métodos:
    def get_object(self):
        excerp, created = Excerp.objects.get_or_create(id = self.kwargs['pk'])
        return excerp
    
    def form_valid(self, form):
        """ Cuando el formulario se envía, el campo foreign key USER lo tomará del usuario logueado """
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ExcerpDeleteView(DeleteView):
    model = Excerp
    success_url = reverse_lazy('excerp-create')

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.delete()
        return self.redirect_to_response(success_url)
    
    def redirect_to_response(self, success_url):
        return HttpResponseRedirect(success_url)