from django.urls import path
from . import views
from .views import upload_expense, expense_list

urlpatterns = [
    path('', upload_expense, name='upload_expense'),
    path('upload/', views.upload_expense, name='upload_expense'),
    path('expenses/', views.expense_list, name='expense_list'),
    path('list/', expense_list, name='expense_list'),
    path('export-csv/', views.export_expenses_csv, name='export_expenses_csv'),
]
