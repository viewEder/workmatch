from datetime import date, datetime
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import User
# Envio del correo Electronico:
from django.core.mail import EmailMessage
from django.urls import reverse
from contacto.forms import ContactoForm


# Create your views here.
class UserListView(ListView):
    template_name = 'perfiles/user_list.html'
    model = User
    paginate_by = 3

class UserDetailView(DetailView):
    model = User
    template_name = 'perfiles/user_detail.html'
    age_user = 0
    contacto_form = ContactoForm()

    def get_object(self):
        return get_object_or_404(User, username=self.kwargs['username'])
    
    def post(self, request, *args, **kwargs):
        
        # Envio del correo electronico:
        if request.method == 'POST':
            self.contacto_form = ContactoForm(data=request.POST)

            if self.contacto_form.is_valid():
                email = request.POST.get('email', '')
                name = request.POST.get('name', '')
                subject = request.POST.get('subject', '')
                message = request.POST.get('message', '')

                email = EmailMessage(
                subject,
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, message),
                "no-contestar@inbox.mailtrap.io",
                ["ederlatru@gmail.com"],
                reply_to = [email]
            )
            
            try:
                email.send()
                return redirect(reverse('usuarios')+'?ok')
            except:
                # Algo no va bien
                return redirect(reverse('usuarios')+'?fail')
    
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
    
    def get_context_data(self, **kwargs):
        contexto = super().get_context_data(**kwargs)
        usuario_id = self.kwargs['username']
        data = get_object_or_404(User, username=usuario_id)
        
        links = data.links_set.all()
        excerp = data.excerp_set.all()
        proyectos = data.projectdev_set.all()
        habilidades = data.skills_set.all()
        empleos = data.employmenthistory_set.all()
        hechos = data.facts_set.all()
        usuario_fechanace = data.birthday
        self.age_user = self.get_edad(usuario_fechanace)
        academia = data.academy_set.all()

               
        contexto['form'] = self.contacto_form

        contexto['links'] = links
        contexto['excerp'] = excerp
        contexto['academia'] = academia
        contexto['proyectos'] = proyectos
        contexto['habilidades'] = habilidades
        contexto['empleos'] = empleos
        contexto['hechos'] = hechos
        contexto['edad'] = self.age_user

        return contexto
