from rest_framework import viewsets
from rest_framework.decorators import list_route
from rest_framework.permissions import IsAuthenticated

from .serializers import OrderSerializer
from .models import Order
from .permissions import IsBuyerOrSellerOrReadOnly


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    queryset = Order.objects.select_related('buyer', 'listing__seller', 'listing', 'listing__vegetable').all()
    permission_classes = (IsAuthenticated, IsBuyerOrSellerOrReadOnly)
    paginate_by = 10

    def list(self, request):
        ids_str = request.GET.get('ids', None)
        if ids_str:
            values = [int(r) for r in ids_str.split(',')]
            self.queryset = Order.objects.filter(pk__in=values)
        return super(OrderViewSet, self).list(self, request)

    def update(self, request, pk=None):
        return super(OrderViewSet, self).update(request, pk, partial=True)

    @list_route(methods=['get'], permission_classes=[IsAuthenticated])
    def user(self, request):
        self.queryset = self.queryset.filter(buyer=request.user)
        is_active = request.GET.get('active', False)
        if is_active:
            self.queryset = self.queryset.filter(status__in=(Order.STATUS.buyer_placed, Order.STATUS.seller_confirmed))
        return super(OrderViewSet, self).list(self, request)
