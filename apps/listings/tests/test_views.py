from django.test import TestCase

from rest_framework.test import force_authenticate, APITestCase
from model_mommy import mommy

from apps.listings.models import Listing
from apps.vegetables.models import Vegetable
from apps.account.models import User
from apps.utils.tests import console_log


class listingViewSetTest(APITestCase):

    def setUp(self):
        self.user = mommy.make(User, lat=10.027044, lng=76.308028)
        self.user1 = mommy.make(User, lat=10.027044, lng=76.308028)

    def test_01_listing_viewset_retrieve(self):
        new_list = mommy.make(Listing, seller=self.user)
        url = '/api/listings/%s/' % new_list.id
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log('listings viewset', 'retrieve')

    def test_02_listing_viewset_create(self):
        url = '/api/listings/'
        self.client.force_authenticate(user=self.user)
        new_list = mommy.make(Listing, seller=self.user)
        data = {
            'seller': new_list.seller.id,
            'vegetable': new_list.vegetable.id,
            'quantity': new_list.quantity
            }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 201)
        console_log('listings viewset', 'create')

    def test_02_listing_viewset_update(self):
        self.client.force_authenticate(user=self.user)
        mommy.make(Listing, seller=self.user)
        listing = Listing.objects.first()
        url = '/api/listings/%s/' % listing.id
        data = {
            'quantity': 10 
            }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        console_log('listings viewset', 'update')

    def test03_listing_viewset_list(self):
        lising_1 = mommy.make(Listing, seller=self.user)
        listing_2 = mommy.make(Listing, seller=self.user)
        list_3 = mommy.make(Listing, seller=self.user)
        url = '/api/listings/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log('listings viewset', 'list')

    def test04_listing_current_user(self):
        lising_1 = mommy.make(Listing, seller=self.user)
        listing_2 = mommy.make(Listing, seller=self.user1)
        listing_3 = mommy.make(Listing, seller=self.user)
        url = '/api/listings/user/'
        self.client.force_authenticate(user=self.user1)
        response = self.client.get(url, format='json')
        data = response.render()
        self.assertEqual(response.status_code, 200)
        console_log("listings viewset", "retrieve current user's listing")

    def test_05_listing_by_queryparam_ids(self):
        listing_1 = mommy.make(Listing, seller=self.user)
        listing_2 = mommy.make(Listing, seller=self.user1)
        listing_3 = mommy.make(Listing, seller=self.user)
        listing_4 = mommy.make(Listing, seller=self.user)
        url = '/api/listings/?ids=%s, %s' % (listing_1.id, listing_3.id)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log("listings viewset", "retrieve listings by id querystring parameter")

    def test_06_listing_by_queryparam_vegetables(self):
        veg_1 = mommy.make(Vegetable)
        veg_2 = mommy.make(Vegetable)
        self.listing_veg1 = mommy.make(Listing, seller=self.user, vegetable=veg_1)
        self.listing_veg2 = mommy.make(Listing, seller=self.user1, vegetable=veg_2)
        url = '/api/listings/?vegetales=%s, %s' % (veg_1.id, veg_2.id)
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log("listings viewset", "retrieve listings by vegetable id querystring parameter")

    def test_07_listing_by_queryparam_active(self):
        isting_1 = mommy.make(Listing, seller=self.user)
        listing_2 = mommy.make(Listing, seller=self.user1)
        listing_3 = mommy.make(Listing, seller=self.user)
        url = '/api/listings/?active=1'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log("listings viewset", "retrieve listings by active querystring parameter")

    def test08_listings_summary(self):
        lising_1 = mommy.make(Listing, seller=self.user)
        listing_2 = mommy.make(Listing, seller=self.user1)
        listig_3 = mommy.make(Listing, seller=self.user)
        url = '/api/listings/summary/'
        self.client.force_authenticate(user=self.user)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log("listings viewset", "listing summary")
