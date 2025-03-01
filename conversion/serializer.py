from rest_framework import serializers
from .models import Currency, ExchangeRate

class CurrencySerializer(serializers.ModelSerializer):
    """Serializer para la moneda (Currency)"""
    
    class Meta:
        model = Currency
        fields = ['id', 'code', 'name']
    
    def __str__(self):
        return f"{self.code} - {self.name}"

class ExchangeRateSerializer(serializers.ModelSerializer):
    """Serializer para la tasa de cambio (ExchangeRate)"""
    
    base_currency = CurrencySerializer(read_only=True)
    target_currency = CurrencySerializer(read_only=True)

    class Meta:
        model = ExchangeRate
        fields = ['id', 'base_currency', 'target_currency', 'rate', 'date']
    
    def __str__(self):
        return f"1 {self.base_currency.code} = {self.rate} {self.target_currency.code} ({self.date})"
