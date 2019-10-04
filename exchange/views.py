from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView

from exchange.forms.converter import ConverterForm
from exchange.models import CurrencyRate
from exchange.utils import convert


class ExchangeView(TemplateView):
    template_name = "exchange.html"

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(ExchangeView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        availiable_currencies = CurrencyRate.objects.all().values_list('abbreviation', flat=True)

        context['currencies'] = availiable_currencies
        return context

    def post(self, request, *args, **kwargs):
        form = ConverterForm(request.POST)
        if form.is_valid():
            currency_from = form.cleaned_data.get('currency_from')
            currency_to = form.cleaned_data.get('currency_to')

            amount = form.cleaned_data.get('amount')

            result = convert(currency_from, currency_to, amount)

            return JsonResponse(data={'result': result})

        return JsonResponse(data={'errors': form.errors}, status=400)



