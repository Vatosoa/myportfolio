from django.shortcuts import render
from django.utils.translation import gettext as _
from django.utils.timezone import now  # pour automatiser l'année

def home(request):
    return render(request, 'core/home.html', { 'now': now() })

def about(request):
    return render(request, 'core/about.html', { 'now': now() })

def contact(request):
    return render(request, 'core/contact.html', { 'now': now() })

def research(request):
    return render(request, 'core/research.html', { 'now': now() })

def publications(request):
    return render(request, 'core/publications.html', { 'now': now() })

def cv(request):
    return render(request, 'core/cv.html', { 'now': now() })

def projects(request):
    return render(request, 'core/projects.html', { 'now': now() })

def blog(request):
    return render(request, 'core/blog.html', { 'now': now() })

