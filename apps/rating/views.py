from django.shortcuts import render

from rest_framework import viewsets
from .models import Rating
from .serializers import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):	
    serializer_class=RatingSerializer
    queryset=Rating.objects.all()

