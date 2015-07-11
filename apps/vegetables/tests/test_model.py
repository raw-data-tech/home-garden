from django.test import TestCase
from apps.vegetables.models import Vegetable
from apps.utils.tests import console_log

from model_mommy import mommy


class VegetableTestModel(TestCase):

    def setUp(self):
        self.vegetable = mommy.make(Vegetable)

    def test_vegetable(self):
        self.assertTrue(isinstance(self.vegetable, Vegetable))
        console_log('vegetables model', 'model')
