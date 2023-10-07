from django import forms
from .models import Academy

class AcademyCreateForm(forms.ModelForm):
    class Meta:
        model = Academy
        fields = ['type_degree','academy_name','degree_obtained','degree_esp','start_date','finish_date','in_progress']
        widgets = {
            'type_degree': forms.Select(attrs={'class':'form-select'}),
            'academy_name': forms.TextInput(attrs={'class':'form-control'}),
            'degree_obtained': forms.TextInput(attrs={'class':'form-control'}),
            'degree_esp': forms.TextInput(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control'}),
            'finish_date': forms.DateInput(attrs={'class':'form-control'}),
            'in_progress': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }
