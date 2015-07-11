import logging

from django.utils import timezone
from django.db import models, transaction
from django.conf import settings
from django.core.mail import send_mail

from gcm.models import get_device_model
from model_utils.fields import StatusField
from model_utils import Choices
from rest_framework import serializers

from apps.listings.models import Listing
from apps.utils.mail import MailSender

Device = get_device_model()
logger = logging.getLogger(__name__)


class Order(models.Model):
    STATUS = Choices('buyer_placed', 'seller_confirmed', 'buyer_purchased', 'timedout', 'buyer_cancelled', 'seller_rejected')
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='orders')
    listing = models.ForeignKey(Listing, related_name='orders')
    created = models.DateTimeField(default=timezone.now)
    quantity = models.DecimalField(max_digits=5, decimal_places=2)
    remark = models.CharField(max_length=256, null=True, blank=True)
    status = StatusField()

    @property
    def notify_message(self):
        return '%s,%s,%s,%s,%s' % (self.listing.id, self.id, self.buyer.first_name, self.listing.vegetable, self.quantity)

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.validate_quantity()
        super(Order, self).save(*args, **kwargs)
        self.listing.update_quantity_remaining(commit=True)
        self.notify()

    def notify(self):
        # FUTURE check for stauts change
        {
            self.STATUS.buyer_placed: self.notify_seller,
            self.STATUS.buyer_cancelled: self.notify_seller,
            self.STATUS.seller_confirmed: self.notify_buyer,
            self.STATUS.seller_rejected: self.notify_buyer,
        }.get(self.status, lambda x: x)(self.status)

    def validate_quantity(self):
        if (self.listing.quantity_remaining < self.quantity) and not self.id:
            msg = "There's not enough quantity for sale. Only %s Kg remains." % (self.listing.quantity_remaining)
            raise serializers.ValidationError(msg)

    def __unicode__(self):
        return '%s Kg (%s)' % (self.buyer.username, self.quantity)

    def notify_seller(self, key):
        devices = Device.objects.filter(name=self.listing.seller.id)
        if not len(devices):
            return
            # print 'Device not registered'
            # send_mail(
            #     'No Device!', 'Device not registered', settings.EMAIL_HOST_USER, [self.listing.seller.email], fail_silently=False)
        devices.send_message(self.notify_message, collapse_key=key)

    def notify_buyer(self, key):
        devices = Device.objects.filter(name=self.buyer.id)
        if not len(devices):
            return
            # print 'Device not registered'
            # send_mail(
            #     'No Device!', 'Device not registered', settings.EMAIL_HOST_USER, [self.buyer.email], fail_silently=False)
        devices.send_message(self.notify_message, collapse_key=key)

    class Meta:
        ordering = ['-pk']
