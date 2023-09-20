from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.urls import reverse
from .forms import ContactoForm

# Create your views here.
def contact(request):
    contacto_form = ContactoForm()
    template = 'contacto/contacto_form.html'
    contexto = { 'form': contacto_form }

    if request.method == 'POST':
        contacto_form = ContactoForm(data=request.POST)

        if contacto_form.is_valid():
            email = request.POST.get('email', '')
            name = request.POST.get('name', '')
            subject = request.POST.get('subject', '')
            message = request.POST.get('message', '')
            # enviar correo electronico

            # email = EmailMessage(
            #     asunto, # "Haz recibido un nuevo mensaje de contacto"
            #     cuerpo, # "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, message)
            #     email_origen, # "no-contestar@inbox.mailtrap.io"
            #     email,destino, # ["ederlatru@gmail.com"]
            #     reply_to = [email]
            # )

            email = EmailMessage(
                "Haz recibido un nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, message),
                "no-contestar@inbox.mailtrap.io",
                ["ederlatru@gmail.com"],
                reply_to = [email]
            )
            
            try:
                email.send()
                return redirect(reverse('contacto')+'?ok')
            except:
                # Algo no va bien
                return redirect(reverse('contacto')+'?fail')

    return render(request, template, contexto)