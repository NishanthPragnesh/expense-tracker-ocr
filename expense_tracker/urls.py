from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Include accounts URLs (login, logout, register)
    path('accounts/', include('accounts.urls')),

    # Include expenses-related views (upload, expense list, etc.)
    path('upload/', include('expenses.urls')),

    path('', RedirectView.as_view(url='/upload/list/', permanent=False)),
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
