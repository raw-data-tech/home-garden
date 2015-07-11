from rest_framework.test import force_authenticate, APITestCase

from model_mommy import mommy

from apps.account.models import User
from apps.utils.tests import console_log


class UserViewSetTestCase(APITestCase):

    def setUp(self):
        self.user1 = mommy.make(User, lat=10.87, lng=76.65)
        self.user2 = mommy.make(User, lat=10.87, lng=76.65)
        self.user3 = mommy.make(User, lat=10.87, lng=76.65)

    def test_user_viewset_list(self):
        url = '/api/users/'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        console_log('account viewset', 'list')

    def test_user_viewset_update(self):
        user = mommy.make(User, lat=10.87, lng=76.65)
        self.client.force_authenticate(user=user)
        url = '/api/users/%s/' % user.id
        data = {"lat": 15.78}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        console_log('account viewset', 'update')


class ObtainAuthTokenTestCase(APITestCase):

    def test_auth_token(self):
        user = User.objects.create_user(username='tester23',first_name='test', password='abcd1234')
        url = '/api-auth-token/'
        data = {'username': user.username, 'password': 'abcd1234'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)
        console_log('account viewset', 'auth-token')
