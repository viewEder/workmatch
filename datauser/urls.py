from django.urls import path
from .views import AcademyDetailView, AcademyCreateView, AcademyUpdateView, AcademyDeleteView, SkillsCreateView, SkillsUpdateView, SkillsDeleteView, HistoryCreateView, HistoryUpdateView, HistoryDeleteView, ProjectCreateView, ProjectUpdateView, ProjectDeleteView, StackCreateView, FactsCreateView, FactsUpdateView, FactsDeleteView, get_job_data

urlpatterns =[
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name= 'academy-detail'),
    path('academy-add/', AcademyCreateView.as_view(), name= 'academy-create'),
    path('academy-upd/<int:pk>/', AcademyUpdateView.as_view(), name= 'academy-update'),
    path('academy-del/<int:pk>/', AcademyDeleteView.as_view(), name= 'academy-delete'),
    path('skills-add/', SkillsCreateView.as_view(), name= 'skills-create'),
    path('skills-upd/<int:pk>/', SkillsUpdateView.as_view(), name= 'skills-update'),
    path('skills-del/<int:pk>/', SkillsDeleteView.as_view(), name= 'skills-delete'),
    path('history-add/', HistoryCreateView.as_view(), name= 'history-create'),
    path('history-upd/<int:pk>/', HistoryUpdateView.as_view(), name= 'history-update'),
    path('history-del/<int:pk>/', HistoryDeleteView.as_view(), name= 'history-delete'),
    path('project-add/', ProjectCreateView.as_view(), name= 'project-create'),
    path('project-upd/<int:pk>/', ProjectUpdateView.as_view(), name= 'project-update'),
    path('project-del/<int:pk>/', ProjectDeleteView.as_view(), name= 'project-delete'),
    path('stack-add/', StackCreateView.as_view(), name= 'stack-create'),
    path('fact-add/', FactsCreateView.as_view(), name= 'fact-create'),
    path('fact-upd/<int:pk>/', FactsUpdateView.as_view(), name= 'fact-update'),
    path('fact-del/<int:pk>/', FactsDeleteView.as_view(), name= 'fact-delete'),
    path('api/job-data/', get_job_data, name='get_job_data'),
]
