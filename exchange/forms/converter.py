from django import forms
from django.core.exceptions import ValidationError

from exchange.models import CurrencyRate


class ConverterForm(forms.Form):
    currency_from = forms.CharField(max_length=3, min_length=3)
    currency_to = forms.CharField(max_length=3, min_length=3)
    amount = forms.FloatField(min_value=0)

    def clean_currency_from(self):
        currency_from = self.cleaned_data['currency_from']

        if currency_from not in CurrencyRate.objects.all().values_list('abbreviation', flat=True):
            raise ValidationError("Not valid currency")
        return currency_from

    def clean_currency_to(self):
        currency_to = self.cleaned_data['currency_to']
        if currency_to not in CurrencyRate.objects.all().values_list('abbreviation', flat=True):
            raise ValidationError("Not valid currency")
        return currency_to
