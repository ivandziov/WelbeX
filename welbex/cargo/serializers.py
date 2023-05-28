from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer
from rest_framework.utils.serializer_helpers import ReturnDict

from car.models import Car
from car.serializers import CarWithDistanceToCargoSerializer
from cargo.models import Cargo


class CargoCreateSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = '__all__'


class CargoListSerializer(ModelSerializer):
    cars_count = SerializerMethodField()

    def get_cars_count(self, cargo: Cargo) -> int:
        car_queryset = self.context['car_queryset']
        max_distance = self.context.get('max_distance', 450)
        cars_count = 0
        for car in car_queryset:
            distance = car.get_distance_to_cargo(cargo)
            if distance <= int(max_distance):
                cars_count += 1
        return cars_count

    class Meta:
        model = Cargo
        fields = ('pick_up_location', 'delivery_location', 'cars_count')


class CargoUpdateSerializer(ModelSerializer):
    class Meta:
        model = Cargo
        fields = ('weight', 'description')


class CargoDetailSerializer(ModelSerializer):
    cars = SerializerMethodField()

    def get_cars(self, cargo) -> ReturnDict:
        all_cars = Car.objects.all().select_related('location')
        car_data = CarWithDistanceToCargoSerializer(all_cars, many=True, context={'cargo': cargo}).data
        return car_data

    class Meta:
        model = Cargo
        fields = ('pick_up_location',
                  'delivery_location',
                  'weight',
                  'description',
                  'cars',
                  )
