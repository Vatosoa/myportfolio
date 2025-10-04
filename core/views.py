from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.timezone import now  # pour automatiser l'année
from .models import Project, Experience, Publication, SkillCategory, AboutContent, CVFile  # 👈 AJOUTEZ CET IMPORT !


def about(request):
    return render(request, 'core/about.html', { 'now': now() })

def experience(request):
    return render(request, 'core/experience.html', { 'now': now() })

def projects(request):
    return render(request, 'core/projects.html', { 'now': now() })

def publications(request):
    return render(request, 'core/publications.html', { 'now': now() })

def cv(request):
    # Récupère le CV selon la langue
    cv_file = CVFile.objects.filter(language=request.LANGUAGE_CODE, is_active=True).first()
    
    # Si pas de CV dans la langue, prend français par défaut
    if not cv_file:
        cv_file = CVFile.objects.filter(language='fr', is_active=True).first()
    
    return render(request, 'core/cv.html', { 
        'now': now(),
        'cv_file': cv_file
    })

def home(request):
    # Récupère le contenu About selon la langue
    about_content = AboutContent.objects.filter(language=request.LANGUAGE_CODE).first()
    
    # Si pas de contenu dans la langue, prend français par défaut
    if not about_content:
        about_content = AboutContent.objects.filter(language='fr').first()
    
    # Récupère le CV selon la langue
    cv_file = CVFile.objects.filter(language=request.LANGUAGE_CODE, is_active=True).first()
    if not cv_file:
        cv_file = CVFile.objects.filter(language='fr', is_active=True).first()
    
    # Récupère les données pour chaque section
    featured_projects = Project.objects.filter(display_order__lte=3)[:3]
    experiences = Experience.objects.all()[:4]
    publications = Publication.objects.all()[:3]
    skills_categories = SkillCategory.objects.prefetch_related('skills').all()
    
    return render(request, 'core/home.html', {
        'now': now(),
        'about_content': about_content,
        'cv_file': cv_file,
        'featured_projects': featured_projects,
        'experiences': experiences,
        'publications': publications,
        'skills_categories': skills_categories
    })
