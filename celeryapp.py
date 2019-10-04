from __future__ import absolute_import, unicode_literals

import os

import celery
import django
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Volsor.settings')
django.setup()

import celeryconfig
from exchange.tasks import update_rates

print(celery.registry.tasks)


app = Celery('exchange')
app.config_from_object(celeryconfig)
app.autodiscover_tasks()


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    sender.add_periodic_task(
        crontab(hour=0, minute=1),
        update_rates.s(),
    )
    update_rates.delay()