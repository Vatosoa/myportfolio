from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.timezone import now  # pour automatiser l'année

def about(request):
    return render(request, 'core/about.html', { 'now': now() })

def experience(request):
    return render(request, 'core/experience.html', { 'now': now() })

def projects(request):
    return render(request, 'core/projects.html', { 'now': now() })

def publications(request):
    return render(request, 'core/publications.html', { 'now': now() })

def cv(request):
    return render(request, 'core/cv.html', { 'now': now() })
