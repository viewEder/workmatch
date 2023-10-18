from django.urls import path
from .views import ProfileUserView, SignUpUserView, ProfileUserUpdate, ExcerpCreateView
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView, PasswordChangeDoneView, PasswordChangeView

urlpatterns =[
    path('profile/', ProfileUserView.as_view(), name = 'perfil'),
    path('register/', SignUpUserView.as_view(), name = 'registro'),
    path('profile_edit/', ProfileUserUpdate.as_view(), name= 'perfil-edit'),
    path('excerp-add/', ExcerpCreateView.as_view(), name= 'excerp-create'),
    # Agregamos las rutas del modulo auth:
    path('logout/', LogoutView.as_view(), name='logout'),
]