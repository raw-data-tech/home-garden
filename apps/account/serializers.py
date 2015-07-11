from rest_framework import serializers
from .models import User


class UserLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('lat', 'lng', ) 
        # write_only_fields = ()

    def create(self, request):
        return User.objects.create_user(**request)


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'place', 'first_name', 'id', 'lat', 'lng', ) 
        write_only_fields = ('password', )

    def create(self, request):
        return User.objects.create_user(**request)

