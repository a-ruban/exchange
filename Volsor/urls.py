from django.contrib import admin
from django.urls import path

from exchange.views import ExchangeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('convert/', ExchangeView.as_view()),
]
