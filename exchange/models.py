from django.db import models


class CurrencyRate(models.Model):
    name = models.CharField(max_length=100)
    abbreviation = models.CharField(max_length=3, null=False, unique=True)
    current_rate = models.FloatField(null=True)
