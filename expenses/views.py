import requests
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Expense, ExchangeRate
from django.forms.models import model_to_dict
from django.utils import timezone

class ExpenseViewSet(viewsets.ViewSet):
    def list(self, request):
        qs = Expense.objects.all().order_by('-date')
        data = [ model_to_dict(obj) for obj in qs ]
        return Response(data)

    def create(self, request):
        obj = Expense.objects.create(**request.data)
        return Response(model_to_dict(obj), status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        obj = Expense.objects.get(pk=pk)
        return Response(model_to_dict(obj))

    def update(self, request, pk=None):
        obj = Expense.objects.get(pk=pk)
        for field, value in request.data.items():
            setattr(obj, field, value)
        obj.save()
        return Response(model_to_dict(obj))

    def destroy(self, request, pk=None):
        obj = Expense.objects.get(pk=pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ExchangeRateViewSet(viewsets.ViewSet):
    def list(self, request):
        qs = ExchangeRate.objects.all()
        data = [ model_to_dict(obj) for obj in qs ]
        return Response(data)

@api_view(['POST'])
def sync_rates(request):
    try:
        url = 'https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@latest/v1/currencies/inr.json'
        response = requests.get(url, timeout=10)
        data = response.json()

        if not data or 'inr' not in data:
            return Response({'success': False, 'error': 'Unexpected API structure'}, status=400)

        date = data.get('date')
        rates = data.get('inr', {})

        ExchangeRate.objects.all().delete()

        bulk_objects = [
            ExchangeRate(
                base='INR',
                symbol=symbol.upper(),
                rate=float(rate),
                fetched_at=timezone.now()
            )
            for symbol, rate in rates.items()
        ]
        ExchangeRate.objects.bulk_create(bulk_objects)

        return Response({
            'success': True,
            'date': date,
            'count': len(bulk_objects),
            'message': f'Successfully synced {len(bulk_objects)} rates on {date}'
        })

    except Exception as e:
        return Response({'success': False, 'error': str(e)}, status=500)


