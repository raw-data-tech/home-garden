import random

from django.db.models import Sum

from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from apps.listings.utils import get_distance
from apps.utils.monitoring import log_time

from .serializers import ListingSerializer, ListingWithOrderDetailsSerializer, ListingSummarySerializer
from .models import Listing
from apps.vegetables.models import Vegetable
from .permissions import IsSellerOrReadOnly


class ListingViewSet(viewsets.ModelViewSet):
    serializer_class = ListingSerializer
    permission_classes = (IsAuthenticated, IsSellerOrReadOnly)
    paginate_by = 10

    def __init__(self, *args, **kwargs):
        self.filter_by_user = False
        self.sort_by_distance = False
        self.exclude_current_user = False
        super(ListingViewSet, self).__init__(*args, **kwargs)

    def list(self, request):
        self.sort_by_distance = True
        self.exclude_current_user = True and (request.GET.get('ids', None) == None)
        return super(ListingViewSet, self).list(request)

    def retrieve(self, request, pk=None):
        self.serializer_class = ListingWithOrderDetailsSerializer
        return super(ListingViewSet, self).retrieve(request, pk)

    def update(self, request, pk=None):
        return super(ListingViewSet, self).update(request, pk, partial=True)

    @list_route(methods=['get'], permission_classes=[IsAuthenticated])
    def user(self, request):
        self.filter_by_user = True
        self.serializer_class = ListingWithOrderDetailsSerializer
        return super(ListingViewSet, self).list(self, request)

    @list_route(methods=['get'], permission_classes=[IsAuthenticated])
    def summary(self, request):
        summary = []
        active = Listing.objects.select_related('vegetable').active()
        for vegetable in Vegetable.objects.all():
            # qty = sum([l.quantity_remaining for l in active.filter(vegetable=vegetable)])
            qty = sum([l.quantity_remaining for l in active if l.vegetable.id == vegetable.id])
            if qty:
                summary.append({'vegetable': vegetable, 'quantity': qty})
        slz = ListingSummarySerializer(summary, many=True)
        return Response(slz.data)

    def get_queryset(self):
        queryset = Listing.objects.select_related()
        if self.filter_by_user:
            queryset = queryset.filter(seller=self.request.user)
        if self.exclude_current_user:
            queryset = queryset.exclude(seller=self.request.user)
        return queryset

    @log_time
    def filter_queryset(self, queryset):
        self.exclude_current_user = False
        queryset = queryset.filter_by_query_param(self.request)
        if self.sort_by_distance:
            self.attach_distance(queryset)
            queryset = sorted(queryset, key=lambda l: l.distance)
        return queryset

    def get_object(self):
        obj = super(ListingViewSet, self).get_object()
        self.attach_distance([obj])
        return obj

    def attach_distance(self, listings):
        user_lat = self.request.GET.get('lat', self.request.user.lat)
        user_lng = self.request.GET.get('lng', self.request.user.lng)
        for l in listings:
            if l.seller.lat and user_lat:
                t = get_distance(user_lat, user_lng, l.seller.lat, l.seller.lng)
                l.distance = round(t, 1)
