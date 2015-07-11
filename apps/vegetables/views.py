from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import VegetableSerializer
from .models import Vegetable


class VegetableViewSet(viewsets.ReadOnlyModelViewSet):

    serializer_class = VegetableSerializer
    queryset = Vegetable.objects.all()
