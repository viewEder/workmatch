from django.shortcuts import render
# Vistas basadas en Clases:
from django.views.generic.base import TemplateView

# Create your views here.
class IndexPageView(TemplateView):
    # Indicar que template usa esta vista:
    template_name = 'core/index.html'
    dict_context = {
        'titulo': 'Welcome to Camel-ing'
    }

    # Utilizando los métodos de la clase, sobreescribios get:
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.dict_context) 
