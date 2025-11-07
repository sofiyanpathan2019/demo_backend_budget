from django.contrib import admin
from .models import Expense, ExchangeRate

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('title', 'amount', 'category', 'date')

@admin.register(ExchangeRate)
class ExchangeRateAdmin(admin.ModelAdmin):
    list_display = ('base', 'symbol', 'rate', 'fetched_at')
