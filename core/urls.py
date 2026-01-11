# core/urls.py
from django.urls import path
from django_distill import distill_path, distill_re_path
from . import views
from django.conf import settings

# Fonction pour générer les langues disponibles
def get_languages():
    for lang_code, _ in settings.LANGUAGES:
        yield {'lang': lang_code}

# Fonction pour chaque vue avec langue
def get_home_urls():
    for lang_code, _ in settings.LANGUAGES:
        yield {'lang': lang_code}
        # Page d'accueil par défaut sans langue
        if lang_code == 'en':  # Par défaut en anglais
            yield {'lang': ''}

urlpatterns = [
    # Pages avec support multi-langue
    distill_path('', views.home, name='home', 
                distill_file='{lang}/index.html',
                distill_func=get_home_urls),
    
    distill_path('about/', views.about, name='about',
                distill_file='{lang}/about/index.html',
                distill_func=get_languages),
    
    distill_path('projects/', views.projects, name='projects',
                distill_file='{lang}/projects/index.html',
                distill_func=get_languages),
    
    distill_path('experience/', views.experience, name='experience',
                distill_file='{lang}/experience/index.html',
                distill_func=get_languages),
    
    distill_path('publications/', views.publications, name='publications',
                distill_file='{lang}/publications/index.html',
                distill_func=get_languages),
    
    distill_path('cv/', views.cv, name='cv',
                distill_file='{lang}/cv/index.html',
                distill_func=get_languages),
]