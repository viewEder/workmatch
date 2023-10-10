"""
URL configuration for src project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# Opciones para ver imagenes:
from django.conf import settings
from django.conf.urls.static import static
from messenger.urls import messenger_patterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('core.urls')),
    # Para implementar el login
    path('accounts/', include('django.contrib.auth.urls') ),
    # datauser:
    path('users/',include('datauser.urls')),
    # registration
    path('user/',include('registration.urls')),
    # perfiles
    path('users/',include('perfiles.urls')),
    # contacto:
    path('users/contacto', include('contacto.urls')),
    # messenger:
    path('chat/', include(messenger_patterns)),
    
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

