from django.urls import path
from .views import ProfileUserView, SignUpUserView

urlpatterns =[
    path('profile/', ProfileUserView.as_view(), name = 'perfil'),
    path('register/', SignUpUserView.as_view(), name = 'registro'),
]