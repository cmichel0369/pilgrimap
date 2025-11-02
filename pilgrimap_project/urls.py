from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hostels.urls')),
    path('accounts/', include('accounts.urls')),  # ✅ pour login/signup/logout
]
