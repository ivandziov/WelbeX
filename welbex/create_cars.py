import random
import os
from django import setup

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'welbex.settings')
setup()

from location.models import Location
from car.models import Car


def create_cars(count: int):
    if Car.objects.exists():
        return
    cars = []
    number = 1000
    locations = Location.objects.all()[:count]
    for _ in range(count):
        car_number = f'{number}A'
        cars.append(
            Car(number=car_number,
                load_capacity=1,
                location=random.choice(locations),
                )
        )
        number += 1
    Car.objects.bulk_create(cars)


create_cars(20)
