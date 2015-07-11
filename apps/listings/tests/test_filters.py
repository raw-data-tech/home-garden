from django.test import TestCase

from model_mommy import mommy

from rest_framework.test import force_authenticate, APITestCase

from apps.vegetables.models import Vegetable
from apps.listings.models import Listing
from apps.account.models import User
# from apps.listings.managers import filter_by_query_param
from apps.utils.tests import console_log

class Request:
    GET = {}

    def __init__(self, GET):
        self.GET = GET 
        

class ListingFilterTestCase(APITestCase):

    def setUp(self):
        self.veg1 = mommy.make(Vegetable)
        self.veg2 = mommy.make(Vegetable)
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.user1 = mommy.make(User, lat=10.027044, lng=76.308028)
        self.listing = mommy.make(Listing, seller=self.user)
        self.listing_veg1 = mommy.make(Listing, seller=self.user, vegetable=self.veg1)
        self.listing_veg2 = mommy.make(Listing, seller=self.user1, vegetable=self.veg2)
        self.listing_inactive = mommy.make(Listing, seller=self.user1, is_cancelled=True, vegetable=self.veg2)

    def test_filter_by_id(self):
        idstr = '%s, %s' % (self.listing_veg1.id, self.listing_veg2.id)
        list_dict = {'ids': idstr}
        request = Request(list_dict)
        filtered_list = Listing.objects.filter_by_query_param(request)
        self.assertTrue(self.listing_veg1 in  filtered_list)
        self.assertTrue(self.listing_veg2 in  filtered_list)
        self.assertFalse(self.listing in filtered_list)
        console_log('listings filters', 'filter by ids')

    def test_filter_by_active(self):
        list_dict = {'active': 1}
        request = Request(list_dict)
        filtered_list = Listing.objects.filter_by_query_param(request)
        self.assertTrue(self.listing_veg1 in  filtered_list)
        self.assertTrue(self.listing_veg2 in  filtered_list)
        self.assertFalse(self.listing_inactive in filtered_list)
        console_log('listings filters', 'filter by active')

    def test_filter_by_vegetable(self):
        list_dict = {'vegetable': self.veg1.id}
        request = Request(list_dict)
        filtered_list = Listing.objects.filter_by_query_param(request)
        self.assertTrue(self.listing_veg1 in  filtered_list)
        self.assertFalse(self.listing_veg2 in  filtered_list)
        console_log('listings filters', 'filter by vegetable')
