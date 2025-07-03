from django.shortcuts import render, redirect
from .forms import ExpenseForm
from .models import Expense
from PIL import Image
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

def expense_list(request):
    expenses = Expense.objects.all().order_by('-date')
    return render(request, 'expenses/expense_list.html', {'expenses': expenses})
