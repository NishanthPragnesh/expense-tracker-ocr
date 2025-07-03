from django.contrib.auth.models import User
from django.db import models

class Expense(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    receipt = models.ImageField(upload_to='receipts/')
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.title
