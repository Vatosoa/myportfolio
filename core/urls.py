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
]

