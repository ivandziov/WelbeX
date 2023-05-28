from django.db import models

from car.validators import validate_car_number
from cargo.models import Cargo
from common.validators import validate_range
from location.models import Location
from geopy.distance import geodesic


class Car(models.Model):
    number = models.CharField(max_length=5, unique=True, validators=[validate_car_number])
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, blank=True, null=True)
    load_capacity = models.PositiveIntegerField(validators=[validate_range(1, 1000)])

    class Meta:
        db_table = 'car'

    def get_distance_to_cargo(self, cargo: Cargo):
        cargo_location = cargo.pick_up_location
        car_location = self.location
        cargo_coordinates = (cargo_location.latitude, cargo_location.longitude)
        car_coordinates = (car_location.latitude, car_location.longitude)
        distance = geodesic(car_coordinates, cargo_coordinates).miles

        return distance

