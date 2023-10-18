from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Excerp


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

class ProfileUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'tipo_id', 'identification', 'photo', 'country', 'city', 'addres', 'phone', 'birthday', 'ocupation_job', 'relocate']
        widgets = {
            'username':  forms.TextInput(attrs={'class': 'form-control'}),
            'first_name':  forms.TextInput(attrs={'class': 'form-control'}),
            'last_name':  forms.TextInput(attrs={'class': 'form-control'}),
            'tipo_id':  forms.Select(attrs={'class': 'form-select'}),
            'identification':  forms.TextInput(attrs={'class': 'form-control'}),
            'photo':  forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'country':  forms.TextInput(attrs={'class': 'form-control'}),
            'city':  forms.TextInput(attrs={'class': 'form-control'}),
            'addres':  forms.TextInput(attrs={'class': 'form-control'}),
            'phone':  forms.TextInput(attrs={'class': 'form-control'}),
            'birthday':  forms.DateInput(attrs={'class': 'form-control'}),
            'ocupation_job': forms.TextInput(attrs={'class': 'form-control'}),
            'relocate': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }

class ExcerpCreateForm(forms.ModelForm):

    class Meta:
        model = Excerp
        fields = ['excerption_type', 'content']
        widgets = {
            'excerption_type':  forms.Select(attrs={'class': 'form-select'}),
            'content':  forms.Textarea(attrs={'class':'form-control', 'rows':'3'})
        }
