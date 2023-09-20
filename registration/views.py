from typing import Optional, Type
from django.forms.models import BaseModelForm
from django.shortcuts import render
from datetime import datetime
from django.views.generic.base import TemplateView
from django.views.generic import CreateView
from .models import User, Links, Excerp
from datauser.models import Academy, ProjectDev, Skills, EmploymentHistory, HobbiesExtras, Facts
from .forms import SingUpUserFormWithEmail
from django.urls import reverse_lazy
from django import forms

# Create your views here.
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

    def get_edad(self, fecha_nacimiento):
        
        try:
            if datetime.now().month <= fecha_nacimiento.month and datetime.now().day <= fecha_nacimiento.day:
                # Si el mes y el día actual es menor o igual al del nacimiento
                edad = (datetime.now().year-1) - fecha_nacimiento.year
            else:
                edad = datetime.now().year - fecha_nacimiento.year
        except:
            edad = 'No es posible calcular la edad'

        return edad


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
        self.age_user = self.get_edad(fechanace)
        
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
            if hobbies.hobby not in self.hobbies:
                self.hobbies.append(hobbies.hobby)

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