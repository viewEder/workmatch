from django.urls import path
from .views import AcademyDetailView, AcamedyListView, AcademyCreateView, SkillsCreateView, HistoryCreateView, ProjectCreateView, AcademyCreateView

urlpatterns =[
<<<<<<< HEAD
    # path('academy-list/', AcamedyListView.as_view(), name = 'academy-list'),
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name= 'academy-detail'),
    path('academy-add/', AcademyCreateView.as_view(), name= 'academy-create'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 3e49c2810146763acfaf5a27b52d3e270546a905
=======
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name= 'academy-detail'),
    path('academy-add/', AcademyCreateView.as_view(), name= 'academy-create'),
    path('skills-add/', SkillsCreateView.as_view(), name= 'skills-create'),
    path('history-add/', HistoryCreateView.as_view(), name= 'history-create'),
    path('project-add/', ProjectCreateView.as_view(), name= 'project-create'),
]
>>>>>>> 35d0a57598cb14328213487a6dd9fea33da2f79f
