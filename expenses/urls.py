from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ExpenseViewSet, ExchangeRateViewSet, sync_rates

router = DefaultRouter()
router.register(r'expenses', ExpenseViewSet,basename='expense')
router.register(r'rates', ExchangeRateViewSet,basename='exchangerate')

urlpatterns = [
    path('', include(router.urls)),
    path('sync-rates/', sync_rates, name='sync_rates'),
]
