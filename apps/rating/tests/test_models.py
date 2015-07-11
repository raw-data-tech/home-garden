from django.test import TestCase

from model_mommy import mommy

from apps.account.models import User
from apps.rating.models import Rating
from apps.orders.models import Order
from apps.listings.models import Listing
from apps.utils.tests import console_log


class RatingModelTest(TestCase):

    def setUp(self):
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.listing = mommy.make(Listing, seller=self.user)
        self.order = mommy.make(Order, listing=self.listing, quantity=0.01)
        self.rating = mommy.make(Rating, order=self.order)

    def test_rating(self):
        self.assertTrue(isinstance(self.rating, Rating)) 
        console_log('rating model', 'model')
