# converter/models.py
from django.db import models

class ConversionHistory(models.Model):
    amount = models.FloatField()
    from_currency = models.CharField(max_length=3)
    to_currency = models.CharField(max_length=3)
    converted_amount = models.FloatField()
    conversion_rate = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.amount} {self.from_currency} to {self.to_currency} at {self.conversion_rate}"