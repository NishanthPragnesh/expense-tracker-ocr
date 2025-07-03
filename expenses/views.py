from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from django.contrib.auth.decorators import login_required
from PIL import Image
from django.db.models import Q
from datetime import datetime
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
    title_query = request.GET.get('title', '')
    min_amount = request.GET.get('min_amount', '')
    max_amount = request.GET.get('max_amount', '')
    start_date = request.GET.get('start_date', '')
    end_date = request.GET.get('end_date', '')

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
    if sort_by == 'amount_asc':
        expenses = expenses.order_by('amount')
    elif sort_by == 'amount_desc':
        expenses = expenses.order_by('-amount')
    elif sort_by == 'date_asc':
        expenses = expenses.order_by('date')
    elif sort_by == 'date_desc':
        expenses = expenses.order_by('-date')

    return render(request, 'expenses/expense_list.html', {'expenses': expenses})

