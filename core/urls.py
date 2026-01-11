# core/urls.py
from django.urls import path
from django_distill import distill_path
from . import views

# Fonction simple pour itérer sur les langues
def get_all_languages():
    # Retourne juste une liste vide car i18n_patterns gère l'argument 'lang'
    # Mais distill a besoin d'un dictionnaire vide par page pour confirmer la génération
    yield {}
    
# core/urls.py
urlpatterns = [
    # La vue 'home' (qui utilise base.html + index.html de Django) 
    # doit devenir un fichier physique 'index.html' pour GitHub
    distill_path('', views.home, name='home', distill_file='index.html'),

    # La vue 'about' doit devenir 'about/index.html'
    distill_path('about/', views.about, name='about', distill_file='about/index.html'),
    distill_path('projects/', views.projects, name='projects', distill_file='projects/index.html'),
    distill_path('experience/', views.experience, name='experience', distill_file='experience/index.html'),
    distill_path('publications/', views.publications, name='publications', distill_file='publications/index.html'),
    distill_path('cv/', views.cv, name='cv', distill_file='cv/index.html'),
]

