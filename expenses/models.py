from django.db import models

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Transport', 'Transport'),
        ('Utilities', 'Utilities'),
        ('Shopping', 'Shopping'),
        ('Other', 'Other'),
    ]
    title = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    date = models.DateField()

    def __str__(self):
        return f"{self.title} - {self.amount}"

class ExchangeRate(models.Model):
    base = models.CharField(max_length=10, default="INR")
    symbol = models.CharField(max_length=10)
    rate = models.FloatField()
    fetched_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-fetched_at']

    def __str__(self):
        return f"{self.base}->{self.symbol} {self.rate}"
