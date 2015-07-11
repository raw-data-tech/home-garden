from rest_framework import serializers
from .models import Vegetable


class VegetableSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vegetable
        fields = ('name_en', 'name_ml', 'price_retail', 'price_wholesale', 'image_url', 'id') 
