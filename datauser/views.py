from django.shortcuts import render
# Vistas basadas en Clases:
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView

from .models import Academy, ProjectDev, Skills, Stack, EmploymentHistory, HobbiesExtras, Facts

# Create your views here.
class AcademyDetailView(DetailView):
    model = Academy

class AcamedyListView(ListView):
    model = Academy

class EmploymentHistoryListView(ListView):
    model = EmploymentHistory