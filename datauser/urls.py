from django.urls import path
from .views import AcademyDetailView, AcamedyListView, AcademyCreateView

urlpatterns =[
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name= 'academy-detail'),
    path('academy-add/', AcademyCreateView.as_view(), name= 'academy-create'),
<<<<<<< HEAD
]
=======
]
>>>>>>> 3e49c2810146763acfaf5a27b52d3e270546a905
