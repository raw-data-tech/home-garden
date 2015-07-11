import datetime
import threading
import sys

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.db import models, transaction
from django.conf import settings

from gcm.models import get_device_model
from rest_framework import serializers

from apps.vegetables.models import Vegetable
from apps.account.models import User

from .utils import get_distance
from .managers import ListingQuerySet

Device = get_device_model()


class Listing(models.Model):
    seller = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='listings')
    vegetable = models.ForeignKey(Vegetable, related_name='listings')
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(default=timezone.now)
    timeout_in_hours = models.PositiveSmallIntegerField(default=56)
    is_cancelled = models.BooleanField(default=False)
    quantity_remaining = models.DecimalField(max_digits=5, decimal_places=2)
    expiry_date = models.DateTimeField(default=timezone.now()+datetime.timedelta(hours=56))

    distance = 1000

    objects = ListingQuerySet.as_manager()

    @property
    def is_timed_out(self):
        return False
        dead_line = self.created + datetime.timedelta(hours=self.timeout_in_hours)
        return timezone.now() > dead_line

    @property
    def is_active(self):
        return not(self.is_cancelled or (self.quantity_remaining==0) or self.expiry_date>timezone.now())

    def notify_created(self):
        # TODO performance check
        message = '%s,%s,%s' % (self.id,  self.vegetable, self.quantity,)
        users = [user for user in User.objects.exclude(id=self.seller.id) if bool(user.lat)]
        target_users = [user.id for user in users if get_distance(user.lat, user.lng, self.seller.lat, self.seller.lng) <= 30]
        target_devices = Device.objects.filter(name__in=target_users)
        target_devices.send_message(message, collapse_key='sale')

    @transaction.atomic
    def save(self, *args, **kwargs):
        if not self.seller.lat:
            msg = "Seller has no location."
            raise serializers.ValidationError(msg)
        self.update_quantity_remaining()
        self.expiry_date = timezone.now() + datetime.timedelta(hours=self.timeout_in_hours)
        super(Listing, self).save(*args, **kwargs)

    def update_quantity_remaining(self, commit=False):
        self.quantity_remaining = self.quantity - sum([o.quantity for o in self.orders.all()])
        if commit:
            super(Listing, self).save()

    def __unicode__(self):
        return '%s - %s Kg(%s Kg available)' % (self.vegetable.name_en, self.quantity, self.quantity_remaining)

    class Meta:
        ordering = ['-pk']


# signal causes test_db to fail to delete after running
@receiver(post_save, sender=Listing)
def _on_new_listing(sender, instance=None, created=False, **kwargs):
    if 'test' in sys.argv:
        return
    if created and instance:
        t = threading.Thread(target=instance.notify_created)
        t.start()
