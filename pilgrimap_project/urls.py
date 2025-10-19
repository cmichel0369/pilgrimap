# pilgrimap_project/urls.py

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hostels.urls')),  # Inclusion des URLs de ton app "hostels"
    path('', include('accounts.urls')),
    # ... autres routes ...
    path('', include('hostels.urls')),  # ou 'accounts.urls'
]

# Pour les fichiers média (si tu en utilises)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)