from rest_framework import serializers
from apps.account.serializers import UserSerializer

from .models import Order
from apps.listings.serializers import ListingMiniSerializer


class OrderSerializer(serializers.ModelSerializer):
    listing_details = serializers.SerializerMethodField()
    buyer_details = serializers.SerializerMethodField()

    def get_buyer_details(self, obj):
        return UserSerializer(obj.buyer).data

    def get_listing_details(self, obj):
        return ListingMiniSerializer(obj.listing).data

    def create(self, request):
        request['buyer'] = self.context['request'].user
        return super(OrderSerializer, self).create(request)

    class Meta:
        model = Order
        read_only_fields = ('buyer', 'created', )
        fields = ('id', 'listing', 'buyer', 'quantity', 'created', 'remark', 'status', 'buyer_details', 'listing_details')

