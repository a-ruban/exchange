from exchange.models import CurrencyRate


def convert(currency_from, currency_to, amount):
    """
    Convert provided amount of one currency to another.
    """
    rate_from = CurrencyRate.objects.filter(abbreviation=currency_from).values_list('current_rate', flat=True)[0]
    rate_to = CurrencyRate.objects.filter(abbreviation=currency_to).values_list('current_rate', flat=True)[0]

    return rate_to / rate_from * amount
