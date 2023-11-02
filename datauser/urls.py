from django.urls import path
from .views import AcademyDetailView, AcademyCreateView, SkillsCreateView, HistoryCreateView, ProjectCreateView, AcademyCreateView, StackCreateView, FactsCreateView, get_job_data

urlpatterns =[
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name= 'academy-detail'),
    path('academy-add/', AcademyCreateView.as_view(), name= 'academy-create'),
    path('skills-add/', SkillsCreateView.as_view(), name= 'skills-create'),
    path('history-add/', HistoryCreateView.as_view(), name= 'history-create'),
    path('project-add/', ProjectCreateView.as_view(), name= 'project-create'),
    path('stack-add/', StackCreateView.as_view(), name= 'stack-create'),
    path('fact-add/', FactsCreateView.as_view(), name= 'fact-create'),
    path('api/job-data/', get_job_data, name='get_job_data'),
]
