from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.upload_expense, name='upload_expense'),
    path('expenses/', views.expense_list, name='expense_list'),
]
