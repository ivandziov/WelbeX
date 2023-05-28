import random

from celery import shared_task
from django.db import transaction

from car.models import Car
from location.models import Location


@shared_task
@transaction.atomic
def change_location_on_all_cars():
    car_queryset = Car.objects.select_for_update()
    locations = Location.objects.all()
    update_list = []
    for car in car_queryset:
        location = random.choice(locations)
        car.location = location
        update_list.append(car)
    Car.objects.bulk_update(update_list, ['location'])



