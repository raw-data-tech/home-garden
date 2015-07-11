import datetime
from django.utils import timezone
from django.db import models

from apps.account.models import User
from apps.orders.models import Order

# rating =[(x, x) for x in [1,2,3,4,5]]
rating = (
    (1,1),
    (2,2),
    (3,3),
    (4,4),
    (5,5),
         )


class Rating(models.Model):
    user = models.ForeignKey(User, related_name='ratings')
    order = models.ForeignKey(Order,related_name='ratings')
    rating = models.PositiveIntegerField(choices=rating, verbose_name='rating')
    remark = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)


    def __unicode__(self):
        return str(self.user)
