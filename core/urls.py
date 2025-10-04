from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 Page d'accueil principale
    path('about/', views.about, name='about'),
    path('experience/', views.experience, name='experience'),
    path('projects/', views.projects, name='projects'), 
    path('publications/', views.publications, name='publications'),
    path('cv/', views.cv, name='cv'),
]