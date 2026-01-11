from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.http import HttpResponseRedirect
from django.utils import translation

from django.conf import settings
from django.conf.urls.static import static

def redirect_to_language(request):
    lang = translation.get_language_from_request(request, check_path=False)
    return HttpResponseRedirect(f'/{lang}/')

# portfolio_site/urls.py
urlpatterns = [
    path('admin/', admin.site.urls),
    path('i18n/', include('django.conf.urls.i18n')),
    # Supprimez i18n_patterns pour la génération statique si possible
    # OU gardez-le mais assurez-vous que core.urls ne demande pas d'arguments
    path('', include('core.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)