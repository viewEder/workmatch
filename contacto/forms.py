"""
    Archivo para el formulario de envio de correos
"""
from django import forms

class ContactoForm(forms.Form):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'class':'form-control'}))
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    subject = forms.CharField(required=True, widget=forms.TextInput(attrs={'class':'form-control'}))
    message = forms.CharField(required=True, widget=forms.Textarea(attrs={'class':'form-control', 'rows':'4'}))