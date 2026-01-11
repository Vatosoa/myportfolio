#!/usr/bin/env python
import os
import sys
import shutil
from pathlib import Path
from django.core.management import execute_from_command_line

def generate_static_site():
    """Génère le site statique directement à la racine (sans sous-dossiers de langue)"""
    
    # Configuration Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
    
    # Force une SECRET_KEY si elle est vide
    if not os.environ.get('SECRET_KEY'):
        os.environ['SECRET_KEY'] = 'django_secret_key_static_build'
    
    # Chemins
    base_dir = Path(__file__).parent
    dist_dir = base_dir / 'dist'
    static_dir = base_dir / 'static'
    media_dir = base_dir / 'media'
    
    # Nettoyage du dossier dist existant
    if dist_dir.exists():
        print(f"🧹 Nettoyage de l'ancien dossier dist...")
        shutil.rmtree(dist_dir)
    
    try:
        # 1. Générer le site statique (le index.html sera créé à la racine de dist)
        print("🚀 Génération du site statique avec django-distill...")
        sys.argv = ['manage.py', 'distill-local', 'dist', '--force', '--collectstatic']
        execute_from_command_line(sys.argv)
        
        # 2. Copier les fichiers statiques (CSS, JS, Images)
        # On les place dans dist/static car votre STATIC_URL est '/myportfolio/static/'
        if static_dir.exists():
            print("📦 Copie des fichiers statiques vers dist/static/...")
            dest_static = dist_dir / 'static'
            shutil.copytree(static_dir, dest_static, dirs_exist_ok=True)
        else:
            print("⚠️ Aucun dossier 'static' source trouvé")
        
        # 3. Copier les médias (Photos de profil, etc.)
        if media_dir.exists():
            print("🖼️ Copie des fichiers médias vers dist/media/...")
            dest_media = dist_dir / 'media'
            shutil.copytree(media_dir, dest_media, dirs_exist_ok=True)
        else:
            print("⚠️ Aucun dossier 'media' source trouvé")

        print(f"✅ Site statique généré avec succès dans : {dist_dir}")
        print(f"👉 L'entrée principale est : {dist_dir}/index.html")
            
    except Exception as e:
        print(f"❌ Erreur lors de la génération : {e}")
        sys.exit(1)

if __name__ == '__main__':
    generate_static_site()
