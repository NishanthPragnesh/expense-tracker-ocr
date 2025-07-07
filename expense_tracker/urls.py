from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from expenses import views
from django.http import HttpResponse
import os
print("📂 Current URLs file loaded from:", os.path.abspath(__file__))

urlpatterns = [
    path('', lambda request: HttpResponse("✅ ROOT URL IS WORKING")),
    path('test/', lambda request: HttpResponse("It works!")),
    path('', views.redirect_to_dashboard_or_login, name='home'),  # Root redirect
    path('admin/', admin.site.urls),
    path('upload/', views.upload_expense, name='upload_expense'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('accounts/', include('django.contrib.auth.urls')),  # Login/Logout
    path('dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('export/csv/', views.export_expenses_csv, name='export_expenses_csv'),
]

# Static & Media (for dev only)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
