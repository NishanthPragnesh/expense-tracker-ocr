from django.contrib import admin
from django.urls import path
from expenses import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', views.upload_expense, name='upload_expense'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('accounts/', include('accounts.urls')),
]

# Media file serving in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
