from django.urls import path
from .views import AcademyDetailView, AcamedyListView, AcademyCreateView, SkillsCreateView, HistoryCreateView, ProjectCreateView, AcademyCreateView

urlpatterns =[
    path('academy-list/', AcamedyListView.as_view(), name = 'academy-list'),
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name= 'academy-detail'),
    path('academy-add/', AcademyCreateView.as_view(), name= 'academy-create'),
    path('skills-add/', SkillsCreateView.as_view(), name= 'skills-create'),
    path('history-add/', HistoryCreateView.as_view(), name= 'history-create'),
    path('project-add/', ProjectCreateView.as_view(), name= 'project-create'),
]
