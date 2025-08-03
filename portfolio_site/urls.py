"""
URL configuration for portfolio_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponseRedirect
from django.utils import translation

from django.conf import settings

def redirect_to_language(request):
    return HttpResponseRedirect(f'/{settings.LANGUAGE_CODE}/')

# Redirige automatiquement vers /en/ ou /fr/ selon la langue du navigateur
# def redirect_to_language(request):
#     lang = translation.get_language_from_request(request)
#     return HttpResponseRedirect(f'/{lang}/')

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('', redirect_to_language),  # 👈 redirection ajoutée ici
]

urlpatterns += i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
)
