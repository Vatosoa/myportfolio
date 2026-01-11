#!/usr/bin/env python
import os
import sys
import shutil
from pathlib import Path
from django.core.management import execute_from_command_line

def generate_static_site():
    """Génère le site statique avec toutes les langues"""
    
    # Configuration Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'portfolio_site.settings')
    
    # Force une SECRET_KEY si elle est vide (uniquement pour la génération statique)
    if not os.environ.get('SECRET_KEY'):
        os.environ['SECRET_KEY'] = 'django_secret_key'
    
    # Chemins
    base_dir = Path(__file__).parent
    dist_dir = base_dir / 'dist'
    static_dir = base_dir / 'static'
    media_dir = base_dir / 'media'
    
    # Sauvegarde du dossier dist existant si besoin
    backup_dir = None
    if dist_dir.exists():
        backup_dir = base_dir / 'dist_backup'
        print(f"⚠️  Sauvegarde de l'ancien site dans {backup_dir}")
        if backup_dir.exists():
            shutil.rmtree(backup_dir)
        shutil.move(dist_dir, backup_dir)
    
    try:
        # Générer le site statique
        print("Génération du site statique...")
        sys.argv = ['manage.py', 'distill-local', 'dist', '--force', '--collectstatic']

        execute_from_command_line(sys.argv)
        
        # Vérifier que la génération a réussi
        if not dist_dir.exists():
            raise RuntimeError("La génération a échoué : dossier 'dist' non créé")
        
        # Copier les fichiers statiques
        print("Copie des fichiers statiques...")
        if static_dir.exists():
            # Copier dans chaque dossier de langue
            for lang in ['fr', 'en']:
                lang_static_dir = dist_dir / lang / 'static'
                lang_static_dir.mkdir(parents=True, exist_ok=True)
                # Copier les fichiers statiques
                for item in static_dir.iterdir():
                    dest = lang_static_dir / item.name
                    if item.is_dir():
                        shutil.copytree(item, dest, dirs_exist_ok=True)
                    else:
                        shutil.copy2(item, dest)
        else:
            print("⚠️  Aucun dossier 'static' trouvé")
        
        # Copier les médias (si présents)
        if media_dir.exists():
            print("Copie des fichiers médias...")
            media_dest = dist_dir / 'media'
            shutil.copytree(media_dir, media_dest)
        else:
            print("⚠️  Aucun dossier 'media' trouvé")
        
        # Créer un redirect.html pour la racine
        redirect_html = dist_dir / 'index.html'
        with open(redirect_html, 'w') as f:
            f.write('''<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Redirection</title>
    <script>
        // Rediriger vers /fr/ par défaut
        const lang = navigator.language.startsWith('fr') ? 'fr' : 'en';
        window.location.href = `/${lang}/`;
    </script>
</head>
<body>
    <p>Redirection vers votre langue...</p>
</body>
</html>''')
        
        print(f"✅ Site statique généré avec succès dans {dist_dir}")
        
        # Supprimer la sauvegarde si tout est OK
        if backup_dir and backup_dir.exists():
            shutil.rmtree(backup_dir)
            
    except Exception as e:
        print(f"❌ Erreur lors de la génération: {e}")
        
        # Restaurer la sauvegarde si elle existe
        if backup_dir and backup_dir.exists():
            print("↩️  Restauration de l'ancienne version...")
            if dist_dir.exists():
                shutil.rmtree(dist_dir)
            shutil.move(backup_dir, dist_dir)
        
        sys.exit(1)

if __name__ == '__main__':
    generate_static_site()