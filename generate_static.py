# generate_static.py
#!/usr/bin/env python
import os
import sys
import shutil
from django.core.management import execute_from_command_line

def generate_static_site():
    """Génère le site statique avec toutes les langues"""
    
    # Configuration Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
    
    # Nettoyer le dossier dist précédent
    dist_dir = os.path.join(os.path.dirname(__file__), 'dist')
    if os.path.exists(dist_dir):
        shutil.rmtree(dist_dir)
    
    # Générer le site statique
    print("Génération du site statique...")
    sys.argv = ['manage.py', 'distill-local', 'dist', '--force']
    execute_from_command_line(sys.argv)
    
    # Copier les fichiers statiques
    print("Copie des fichiers statiques...")
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    if os.path.exists(static_dir):
        shutil.copytree(static_dir, os.path.join(dist_dir, 'static'))
    
    # Copier les médias (si présents)
    media_dir = os.path.join(os.path.dirname(__file__), 'media')
    if os.path.exists(media_dir):
        shutil.copytree(media_dir, os.path.join(dist_dir, 'media'))
    
    print(f"✅ Site statique généré dans {dist_dir}")

if __name__ == '__main__':
    generate_static_site()