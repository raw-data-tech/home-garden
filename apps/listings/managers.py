from django.db import models
from django.db.models import Q
from django.utils import timezone

from apps.utils.monitoring import log_time
from .filters import ListingFilter


class ListingQuerySet(models.QuerySet):

    def get_user_sales_kg(self, user, days=7):
        pass
        # quantity = reduce((lambda x,y:x+y),[int(x.quantity) for x in Listing.objects.filter(seller__username=user) & Listing.objects.filter(created__gte=(datetime.date.today() - timedelta(days)))])

    def active(self):
        items = self.filter(Q(is_cancelled=False), Q(quantity_remaining__gt=0), Q(expiry_date__gte=timezone.now()))
        return items

    @log_time
    def filter_by_query_param(self, request):
        queryset = ListingFilter(request, self).get_result()
        return queryset
