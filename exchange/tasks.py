"""
Provide tasks that could be scheduled with Celery.
"""
import json

import requests
from celery import shared_task

from exchange.models import CurrencyRate

UPDATE_CURRENCIES_URL = 'https://openexchangerates.org/api/latest.json'
APP_ID_DEV = '00a7363c89424ab094615f38ccd4295c'


def _get_current_rates(currency_abbreviations):
    """
    Get current rate for each of provided currency-abbreviation.
    """
    params = {
        'app_id': APP_ID_DEV,
        'base': 'USD',
        'symbols': currency_abbreviations
    }
    response_content = json.loads(requests.get(UPDATE_CURRENCIES_URL, params=params).content)

    return response_content.get('rates')


@shared_task
def update_rates():
    """
    Update exchange rates.
    """
    rates_objects = CurrencyRate.objects.all()
    abbreviations = ','.join(rate.abbreviation for rate in rates_objects)

    rates = _get_current_rates(abbreviations)

    for item in rates_objects:
        rate = rates.get(item.abbreviation)
        item.current_rate = rate
        item.save()
