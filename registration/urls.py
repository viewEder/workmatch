from django.urls import path
from .views import ProfileUserView, SignUpUserView, ProfileUserUpdate, ExcerpCreateView, ExcerpUpdateView, ExcerpDeleteView
from django.contrib.auth.views import LogoutView, PasswordResetCompleteView, PasswordResetDoneView, PasswordResetConfirmView, PasswordChangeDoneView, PasswordChangeView

urlpatterns =[
    path('profile/', ProfileUserView.as_view(), name = 'perfil'),
    path('register/', SignUpUserView.as_view(), name = 'registro'),
    path('profile_edit/', ProfileUserUpdate.as_view(), name= 'perfil-edit'),
    path('excerp-add/', ExcerpCreateView.as_view(), name= 'excerp-create'),
    path('excerp-upd/<int:pk>/', ExcerpUpdateView.as_view(), name= 'excerp-update'),
    path('excerp-del/<int:pk>', ExcerpDeleteView.as_view(), name= 'excerp-delete'),
    # Agregamos las rutas del modulo auth:
    path('logout/', LogoutView.as_view(), name='logout'),
]