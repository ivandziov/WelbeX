import os
from datetime import timedelta

from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'welbex.settings')

app = Celery('welbex')
app.config_from_object('django.conf:settings')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()
app.conf.imports = (
    'car.tasks',
)
app.conf.beat_schedule = {
    'set-random-location-to-all-car-every-3-minute': {
        'task': 'car.tasks.change_location_on_all_cars',
        'schedule': timedelta(minutes=3),
    },
}
