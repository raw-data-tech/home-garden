from django.db import models
from django.db.models import Avg


class RatingQuerySet(models.QuerySet):

    @property
    def average(self):
        q1 =self.aggregate(Avg('rating'))
        return q1['rating__avg']
        