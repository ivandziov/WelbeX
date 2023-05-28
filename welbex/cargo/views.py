from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets

from rest_framework.response import Response

from car.models import Car
from cargo.models import Cargo
from cargo.serializers import CargoCreateSerializer, CargoDetailSerializer, CargoUpdateSerializer, CargoListSerializer


class CargoViewSet(viewsets.ViewSet):

    def list(self, request):
        max_weight = request.GET.get('max_weight')
        max_distance_to_cargo = request.GET.get('max_distance')
        cargo_queryset = Cargo.objects.filter(weight__lte=max_weight) if max_weight else Cargo.objects.all()
        cargo_queryset = cargo_queryset.select_related('pick_up_location')
        car_queryset = Car.objects.all().select_related('location')
        serializer = CargoListSerializer(cargo_queryset,
                                         many=True,
                                         context={
                                             'max_distance': max_distance_to_cargo if max_distance_to_cargo else 450,
                                             'car_queryset': car_queryset,
                                         },
                                         )
        data = serializer.data
        return Response(data)

    def create(self, request):
        serializer = CargoCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        obj = get_object_or_404(Cargo.objects.select_related('pick_up_location'), pk=pk)
        serializer = CargoDetailSerializer(obj)
        return Response(serializer.data)

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(Cargo, pk=pk)
        serializer = CargoUpdateSerializer(instance=obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        obj = get_object_or_404(Cargo, pk=pk)
        obj.delete()
        return Response(status.HTTP_204_NO_CONTENT)
