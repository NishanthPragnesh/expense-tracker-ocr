from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.db.models import Q
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
import pytesseract

def upload_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST, request.FILES)
        if form.is_valid():
            expense = form.save()
            try:
                img = Image.open(expense.receipt.path)
                text = pytesseract.image_to_string(img)
                expense.notes = text.strip()[:1000]
                expense.save()
            except Exception as e:
                expense.notes = f"Error reading image: {e}"
                expense.save()
            return redirect('expense_list')
    else:
        form = ExpenseForm()
    return render(request, 'expenses/upload_expense.html', {'form': form})

@login_required
def expense_list(request):
    expenses = Expense.objects.filter(user=request.user)

    # --- Filtering ---
    query = request.GET.get('q', '')
    title_query = request.GET.get('title', '')
    min_amount = request.GET.get('min_amount', '')
    max_amount = request.GET.get('max_amount', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

    if query:
        expenses = expenses.filter(
            Q(title__icontains=query) |
            Q(notes__icontains=query) |
            Q(amount__icontains=query) |
            Q(date__icontains=query)
        )

    if title_query:
        expenses = expenses.filter(title__icontains=title_query)

    if min_amount:
        expenses = expenses.filter(amount__gte=min_amount)

    if max_amount:
        expenses = expenses.filter(amount__lte=max_amount)

    if start_date:
        try:
            start = datetime.strptime(start_date, '%Y-%m-%d')
            expenses = expenses.filter(date__gte=start)
        except ValueError:
            pass

    if end_date:
        try:
            end = datetime.strptime(end_date, '%Y-%m-%d')
            expenses = expenses.filter(date__lte=end)
        except ValueError:
            pass

    # --- Sorting ---
    sort_by = request.GET.get('sort', '')
    if sort_by == 'title_asc':
        expenses = expenses.order_by('title')
    elif sort_by == 'title_desc':
        expenses = expenses.order_by('-title')
    elif sort_by == 'amount_asc':
        expenses = expenses.order_by('amount')
    elif sort_by == 'amount_desc':
        expenses = expenses.order_by('-amount')
    elif sort_by == 'date_asc':
        expenses = expenses.order_by('date')
    elif sort_by == 'date_desc':
        expenses = expenses.order_by('-date')

    return render(request, 'expenses/expense_list.html', {
        'expenses': expenses,
        'query': query,
        'sort': sort_by
    })

@staff_member_required
def admin_dashboard(request):
    total_users = User.objects.count()
    total_expenses = Expense.objects.count()
    latest_expense = Expense.objects.order_by('-id').first()
    
    # Top 5 users by number of expenses
    top_users = User.objects.annotate(expense_count=models.Count('expense')).order_by('-expense_count')[:5]

    context = {
        'total_users': total_users,
        'total_expenses': total_expenses,
        'latest_expense': latest_expense,
        'top_users': top_users,
    }
    return render(request, 'expenses/admin_dashboard.html', context)


