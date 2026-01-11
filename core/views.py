# core/views.py
from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.timezone import now
from django.conf import settings
from django.utils import translation
from .models import Project, Experience, Publication, SkillCategory, AboutContent, CVFile

def set_language_context(request, lang=None):
    """Set language context for static generation"""
    if lang:
        translation.activate(lang)
        request.LANGUAGE_CODE = lang
    
    # Récupère le contenu pour la langue spécifiée
    about_content = AboutContent.objects.filter(language=lang or request.LANGUAGE_CODE).first()
    cv_file = CVFile.objects.filter(language=lang or request.LANGUAGE_CODE, is_active=True).first()
    
    # Fallback en français si besoin
    if not about_content:
        about_content = AboutContent.objects.filter(language='fr').first()
    if not cv_file:
        cv_file = CVFile.objects.filter(language='fr', is_active=True).first()
    
    return {
        'about_content': about_content,
        'cv_file': cv_file,
        'LANGUAGE_CODE': lang or request.LANGUAGE_CODE,
    }

def home(request, lang=None):
    """Vue home adaptée pour distill"""
    context = set_language_context(request, lang)
    context.update({
        'featured_projects': Project.objects.filter(display_order__lte=3)[:3],
        'experiences': Experience.objects.all()[:4],
        'publications': Publication.objects.all()[:3],
        'skills_categories': SkillCategory.objects.prefetch_related('skills').all(),
        'now': now(),
    })
    return render(request, 'base.html', context)