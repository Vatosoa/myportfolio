# core/urls.py
from django.urls import path
from django_distill import distill_path
from . import views

# Fonction simple pour itérer sur les langues
def get_all_languages():
    # Retourne juste une liste vide car i18n_patterns gère l'argument 'lang'
    # Mais distill a besoin d'un dictionnaire vide par page pour confirmer la génération
    yield {}

urlpatterns = [
    # Ne mettez PAS {lang} ici, i18n_patterns s'en occupe
    distill_path('', views.home, name='home', distill_func=get_all_languages),
    distill_path('about/', views.about, name='about', distill_func=get_all_languages),
    distill_path('projects/', views.projects, name='projects', distill_func=get_all_languages),
    distill_path('experience/', views.experience, name='experience', distill_func=get_all_languages),
    distill_path('publications/', views.publications, name='publications', distill_func=get_all_languages),
    distill_path('cv/', views.cv, name='cv', distill_func=get_all_languages),
]
