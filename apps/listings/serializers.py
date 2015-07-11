from rest_framework import serializers
from apps.account.serializers import UserSerializer
from apps.vegetables.serializers import VegetableSerializer

from .models import Listing
from apps.orders.models import Order


class OrderMiniSerializer(serializers.ModelSerializer):
    buyer_details = serializers.SerializerMethodField()

    def get_buyer_details(self, obj):
        return UserSerializer(obj.buyer).data

    class Meta:
        model = Order
        read_only_fields = ('buyer', 'created', 'status', 'remark')
        fields = ('id', 'buyer', 'quantity', 'created', 'status', 'buyer_details', 'remark')

READ_ONLY = ('seller', 'created', 'quantity_remaining', 'is_timed_out')
LIST_MINI_FIELDS = ['id', 'vegetable', 'seller_details', 'quantity', 'vegetable_details', 'is_cancelled', 'created',]
LIST_FIELDS =  LIST_MINI_FIELDS + ['distance', 'quantity_remaining', 'is_timed_out', ]

class ListingSerializer(serializers.ModelSerializer):
    vegetable_details = serializers.SerializerMethodField()
    seller_details = serializers.SerializerMethodField()

    def get_vegetable_details(self, obj):
        return VegetableSerializer(obj.vegetable).data

    def get_seller_details(self, obj):
        return UserSerializer(obj.seller).data

    def create(self, request):
        request['seller'] = self.context['request'].user
        return super(ListingSerializer, self).create(request)

    class Meta:
        model = Listing
        write_only_fields = ('vegetable', )
        read_only_fields = READ_ONLY 
        fields = LIST_FIELDS


class ListingMiniSerializer(ListingSerializer):

    class Meta:
        model = Listing
        write_only_fields = ('vegetable', )
        read_only_fields = READ_ONLY 
        fields = LIST_MINI_FIELDS


class ListingWithOrderDetailsSerializer(ListingSerializer):
    orders = OrderMiniSerializer(many=True, read_only=True)

    class Meta:
        model = Listing
        write_only_fields = ('vegetable', )
        read_only_fields = READ_ONLY 
        fields = LIST_FIELDS + ['orders']


class ListingSummarySerializer(serializers.Serializer):
    vegetable = VegetableSerializer()
    # vegetable = serializers.IntegerField()
    quantity = serializers.DecimalField(max_digits=5, decimal_places=2)
