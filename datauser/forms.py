from django import forms
from .models import Academy, Skills, EmploymentHistory, ProjectDev

class AcademyCreateForm(forms.ModelForm):
    class Meta:
        model = Academy
        fields = ['type_degree','academy_name','degree_obtained','degree_esp','start_date','finish_date','in_progress']
        widgets = {
            'type_degree': forms.Select(attrs={'class':'form-select'}),
            'academy_name': forms.TextInput(attrs={'class':'form-control'}),
            'degree_obtained': forms.TextInput(attrs={'class':'form-control'}),
            'degree_esp': forms.TextInput(attrs={'class':'form-control'}),
            'start_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'finish_date': forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'in_progress': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }


class SkillsCreateForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skill','level','description']
        widgets = {
            'skill': forms.TextInput(attrs={'class':'form-control'}),
            'level': forms.Select(attrs={'class':'form-select'}),
            'description': forms.Textarea(attrs={'class':'form-control', 'rows':5})
        }

class HistoryCreateForm(forms.ModelForm):
    class Meta:
        model = EmploymentHistory
        fields = ['stack','company','position','job_description','start_date','end_date','still_work']
        widgets = {
            'stack': forms.Select(attrs={'class':'form-select'}),
            'company': forms.TextInput(attrs={'class':'form-control'}),
            'position': forms.TextInput(attrs={'class':'form-control'}),
            'job_description': forms.TextInput(attrs={'class':'form-control'}),
            'start_date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'end_date': forms.TextInput(attrs={'class':'form-control', 'type':'date'}),
            'still_work': forms.CheckboxInput(attrs={'class':'form-check-input'}),
        }

class ProjectCreateForm(forms.ModelForm):
    class Meta:
        model = ProjectDev
        fields = ['stack','name_project','resume_project','url_repo','year_production','developing']
        widgets = {
            'stack': forms.Select(attrs={'class':'form-select'}),
            'name_project': forms.TextInput(attrs={'class':'form-control'}),
            'resume_project': forms.TextInput(attrs={'class':'form-control'}),
            'url_repo': forms.TextInput(attrs={'class':'form-control', 'type':'url'}),
            'year_production': forms.NumberInput(attrs={'class':'form-control'}),
            'developing': forms.CheckboxInput(attrs={'class':'form-check-input'})
        }from django import forms
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
