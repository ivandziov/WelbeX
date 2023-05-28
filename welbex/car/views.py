from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets

from rest_framework.response import Response

from car.models import Car
from car.serializers import CarUpdateSerializer


class CarViewSet(viewsets.ViewSet):

    def partial_update(self, request, pk=None):
        obj = get_object_or_404(Car, pk=pk)
        serializer = CarUpdateSerializer(instance=obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK)

