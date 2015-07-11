from decimal import Decimal
import random

from time import sleep

from django.db import transaction
from model_mommy import mommy

from apps.account.models  import User
from apps.orders.models import Listing, Order
from apps.vegetables.models import Vegetable


@transaction.atomic
def run():
    users = []
    index = User.objects.count()
    vegetables = Vegetable.objects.all()
    for i in range(100):
        users.append(mommy.make(User, username='user%s' % str(index + i), lat=10.027044, lng=76.308028))
        sleep(.001)

    prev_user = users[-1]
    for user in users:
        for i in range(5):
            listing = mommy.make(Listing, vegetable = random.choice(vegetables), seller=user, quantity=Decimal(10.0))
            mommy.make(Order, listing=listing, buyer=prev_user, quantity=Decimal(5.0))
            mommy.make(Order, listing=listing, buyer=prev_user, quantity=Decimal(4.0))
        sleep(.001)
        prev_user = user
