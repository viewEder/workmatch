from django.contrib import admin
# Importar los modelos de datos:
from .models import User, Links, Excerp

# Register your models here.
admin.site.register(User)
admin.site.register(Links)
admin.site.register(Excerp)
