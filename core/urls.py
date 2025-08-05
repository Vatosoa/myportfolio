from django.urls import path
from . import views

urlpatterns = [
    path('', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('research/', views.research, name='research'),
    path('publications/', views.publications, name='publications'),
    path('cv/', views.cv, name='cv'),
    path('projects/', views.projects, name='projects'), 
    path('blog/', views.blog, name='blog'),
]