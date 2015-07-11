from django.db import models

from rest_framework import serializers

class Vegetable(models.Model):
    name_en = models.CharField(max_length=64, verbose_name='Name(English)')
    name_ml = models.CharField(max_length=64, verbose_name='Name(Malayalam)')
    image_url = models.URLField(null=True)
    price_retail = models.PositiveIntegerField(null=True)
    price_wholesale = models.PositiveIntegerField(null=True)
    is_deleted = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name_en

    def save(self, *args, **kwargs):
        if self.price_wholesale > self.price_retail:
            raise serializers.ValidationError('wholesale price must not exceed retail price')
        super(Vegetable, self).save(*args, **kwargs)
