# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_quantity_remaining'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 20, 47, 29, 576303)),
            preserve_default=True,
        ),
    ]
