from django.test import TestCase

from model_mommy import mommy

from apps.account.models import User
from apps.utils.tests import console_log


class UserTestModel(TestCase):

    def setUp(self):
        self.person = mommy.make(User)

    def test_user(self):
        self.assertTrue(isinstance(self.person, User))
        console_log('account model', 'model')
