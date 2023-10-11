from django.urls import path
from .views import AcademyDetailView, AcamedyListView, AcademyCreateView

urlpatterns =[
    # path('academy-list/', AcamedyListView.as_view(), name = 'academy-list'),
    path('academy/<int:pk>/', AcademyDetailView.as_view(), name= 'academy-detail'),
    path('academy-add/', AcademyCreateView.as_view(), name= 'academy-create'),
]