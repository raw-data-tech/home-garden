from django.test import TestCase

from model_mommy import mommy

from apps.listings.models import Listing
from apps.account.models import User
from apps.utils.tests import console_log


class ManagerTestCase(TestCase):

    def setUp(self):
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.listing1 = mommy.make(Listing, seller=self.user)
        self.listing2 = mommy.make(Listing, seller=self.user)
        self.listing3 = mommy.make(Listing, seller=self.user)

    def test_active(self):
        self.listing1.is_cancelled = True
        self.listing1.save()
        listings = Listing.objects.active()
        self.assertNotIn(self.listing1, listings)
        console_log('listings manager', 'active')
