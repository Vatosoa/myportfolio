# core/urls.py
from django_distill import distill_path
from . import views

def get_single_page():
    yield {}

urlpatterns = [
    # La home devient physiquement index.html à la racine du projet
    distill_path('', views.home, name='home', 
                 distill_func=get_single_page, 
                 distill_file='index.html'),
]

