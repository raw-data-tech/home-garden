from decimal import Decimal
from django.test import TestCase

from model_mommy import mommy

from apps.orders.models import Order
from apps.listings.models import Listing
from apps.listings.utils import get_distance
from apps.account.models import User
from apps.utils.tests import console_log


class ListingModelTest(TestCase):

    def setUp(self):
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.item = mommy.make(Listing, seller=self.user)

    def test_listing(self):
        self.assertTrue(isinstance(self.item, Listing))
        console_log('listings model', 'model')

    def test_quantity_remaining(self):
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.list_item = mommy.make(Listing, seller=self.user, quantity=Decimal(10.0))
        self.order_item = mommy.make(Order, listing=self.list_item, quantity=Decimal(9.0))
        self.assertEquals(self.list_item.quantity_remaining, Decimal(1.0))
        console_log('listings model', 'quantity_remaining')
       
    def test_active(self):
        self.item.is_cancelled = True
        self.item.save()
        listings = Listing.objects.active()
        self.assertNotIn(self.item, listings)
        console_log('listings model', 'active')


class DistanceTestCase(TestCase):

    def test_distance(self):
        from_lat, from_lng = 10.027044, 76.308028
        to_lat, to_lng = 10.004727, 76.312547
        distace = get_distance(from_lat, from_lng, to_lat, to_lng)
        self.assertEquals(round(distace, 1), 2.5)
        console_log('listings model', 'get_distance')
