from django.test import TestCase
from model_mommy import mommy


from rest_framework.test import APIRequestFactory, force_authenticate
from rest_framework.authtoken.models import Token
from model_mommy import mommy

from apps.listings.models import Listing
from apps.orders.models import Order
from apps.orders.views import OrderViewSet
from apps.listings.views import ListingViewSet
from apps.account.models import User, create_auth_token
from apps.utils.tests import console_log


class OrderViewSetTest(TestCase):

    def setUp(self):
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.user1 = mommy.make(User, lat=10.027044, lng=76.308028)
        self.listing = mommy.make(Listing, seller=self.user, quantity=100)
        self.order = mommy.make(Order, buyer=self.user1, quantity=10, listing=self.listing)
        self.order = mommy.make(Order, buyer=self.user, quantity=10, listing=self.listing)
        self.order = mommy.make(Order, buyer=self.user, quantity=10, listing=self.listing)

    def test_01_order_retrieve(self):
        request = APIRequestFactory().get("")
        force_authenticate(request, user=self.user)
        order_detail = OrderViewSet.as_view({'get': 'retrieve'})
        # giving a low order quantity to ensure it is less than list quantity
        new_order = mommy.make(Order, buyer=self.user, quantity=0.01, listing=self.listing)
        response = order_detail(request, pk=new_order.pk)
        response.render()
        self.assertEqual(response.status_code, 200)
        console_log('orders viewset', 'retrieve')

    def test_02_order_create(self):
        factory = APIRequestFactory()
        # giving a low order quantity to ensure it is less than list quantity
        new_order = mommy.make(Order, buyer=self.user, quantity=0.01, listing=self.listing)
        request = factory.post('', {
            'buyer': new_order.buyer.id,
            'listing': new_order.listing.id,
            'quantity': new_order.quantity, },
        )
        force_authenticate(request, user=self.user)
        order_detail = OrderViewSet.as_view({'post': 'create'})
        response = order_detail(request)
        self.assertEqual(response.status_code, 201)
        console_log('orders viewset', 'create')

    def test_03_order_update(self):
        factory = APIRequestFactory()
        new_order = mommy.make(Order, buyer=self.user, quantity=0.01, listing=self.listing)
        request = factory.put('', {
            'quantity': new_order.quantity, },
        )
        force_authenticate(request, user=self.user)
        order_detail = OrderViewSet.as_view({'put': 'update'})
        response = order_detail(request, pk=new_order.pk)
        self.assertEqual(response.status_code, 200)
        console_log('orders viewset', 'update')

    def test_04_order_per_user(self):
        request = APIRequestFactory().get("/api/orders/user/")
        force_authenticate(request, user=self.user)
        order_list = OrderViewSet.as_view({'get': 'list'})
        response = order_list(request)
        response.render()
        self.assertEqual(response.status_code, 200)
        console_log('orders viewset', 'user list')
