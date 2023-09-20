from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class SingUpUserFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Requerido, asegurese de que sea un correo válido!')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email

