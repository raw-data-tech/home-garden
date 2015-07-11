from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from .managers import AuthUserManager


class User(AbstractUser):
    place = models.CharField(max_length=64, null=True, blank=True)
    address = models.CharField(max_length=128, null=True, blank=True)
    lat = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)
    lng = models.DecimalField(max_digits=12, decimal_places=8, null=True, blank=True)

    objects = AuthUserManager()

    # def save(self, *args, **kwargs):
    #     super(User, self).save(self)
    #     if len(self.password) < 20:
    #         self.set_password(self.password)
    #         super(User, self).save(self)
    #     # return self

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
