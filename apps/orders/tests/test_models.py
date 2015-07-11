from decimal import Decimal

from django.test import TestCase

from model_mommy import mommy

from apps.listings.models import Listing
from apps.orders.models import Order
from apps.account.models import User
from apps.utils.tests import console_log


class OrderModelTest(TestCase):

    def setUp(self):
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.listing = mommy.make(Listing, seller=self.user)
        self.item = mommy.make(Order, quantity=0.01, buyer=self.user, listing=self.listing)

    def test_order(self):
        self.assertTrue(isinstance(self.item, Order))
        console_log('orders model', 'model')

    def test_quantity_decreasing(self):
        listing = mommy.make(Listing, seller=self.user, quantity=10)
        item = mommy.make(Order, quantity=5, buyer=self.user, listing=listing)
        self.assertEquals(listing.quantity_remaining, 5.0)
        console_log('orders model', 'test to check quantity decreasing')
