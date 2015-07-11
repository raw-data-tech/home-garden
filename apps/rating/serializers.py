from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields  =('user','order', 'rating', 'remark', 'date')