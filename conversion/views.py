from rest_framework import viewsets, status
from rest_framework.response import Response
from django.http import Http404
from .models import Currency, ExchangeRate
from .serializer import CurrencySerializer, ExchangeRateSerializer

# ViewSet para Monedas (Currency)
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

    def get_currency(self, currency_id):
        try:
            return Currency.objects.get(id=currency_id)
        except Currency.DoesNotExist:
            return None

    def retrieve(self, request, pk=None):
        currency = self.get_currency(pk)
        if not currency:
            return Response({"res": "La moneda no existe"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CurrencySerializer(currency)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CurrencySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        currency = self.get_currency(pk)
        if not currency:
            return Response({"res": "La moneda no existe"}, status=status.HTTP_404_NOT_FOUND)
        serializer = CurrencySerializer(currency, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        currency = self.get_currency(pk)
        if not currency:
            return Response({"res": "La moneda no existe"}, status=status.HTTP_404_NOT_FOUND)
        currency.delete()
        return Response({"res": "Moneda eliminada"}, status=status.HTTP_204_NO_CONTENT)

# ViewSet para Tasas de Cambio (ExchangeRate)
class ExchangeRateViewSet(viewsets.ModelViewSet):
    queryset = ExchangeRate.objects.all()
    serializer_class = ExchangeRateSerializer

    def get_exchange_rate(self, exchange_rate_id):
        try:
            return ExchangeRate.objects.get(id=exchange_rate_id)
        except ExchangeRate.DoesNotExist:
            return None

    def retrieve(self, request, pk=None):
        rate = self.get_exchange_rate(pk)
        if not rate:
            return Response({"res": "La tasa de cambio no existe"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExchangeRateSerializer(rate)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = ExchangeRateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk=None):
        rate = self.get_exchange_rate(pk)
        if not rate:
            return Response({"res": "La tasa de cambio no existe"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ExchangeRateSerializer(rate, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        rate = self.get_exchange_rate(pk)
        if not rate:
            return Response({"res": "La tasa de cambio no existe"}, status=status.HTTP_404_NOT_FOUND)
        rate.delete()
        return Response({"res": "Tasa de cambio eliminada"}, status=status.HTTP_204_NO_CONTENT)

