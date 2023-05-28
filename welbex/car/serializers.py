from rest_framework import serializers
from .models import Car


class CarWithDistanceToCargoSerializer(serializers.ModelSerializer):
    number = serializers.CharField()
    distance = serializers.SerializerMethodField()

    def get_distance(self, obj):
        cargo = self.context.get('cargo')
        return obj.get_distance_to_cargo(cargo)

    class Meta:
        model = Car
        fields = ('number', 'distance',)


class CarUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Car
        fields = ('location',)

