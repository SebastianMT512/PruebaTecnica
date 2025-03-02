from django.db import models
# Create your models here.

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  
    name = models.CharField(max_length=50)  

    def __str__(self):
        return f"{self.code} - {self.name}"

class ExchangeRate(models.Model):
    base_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="base_rates")
    target_currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="target_rates")
    rate = models.DecimalField(max_digits=10, decimal_places=4)
    date = models.DateField(auto_now_add=True) 

    class Meta:
        unique_together = ('base_currency', 'target_currency', 'date') 

    def __str__(self):
        return f"1 {self.base_currency.code} = {self.rate} {self.target_currency.code} ({self.date})"
