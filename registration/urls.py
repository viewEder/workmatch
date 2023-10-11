from django.urls import path
from .views import ProfileUserView, SignUpUserView, ProfileUserUpdate

urlpatterns =[
    path('profile/', ProfileUserView.as_view(), name = 'perfil'),
    path('register/', SignUpUserView.as_view(), name = 'registro'),
    path('profile_edit/', ProfileUserUpdate.as_view(), name= 'perfil-edit')
<<<<<<< HEAD
]
=======
]
