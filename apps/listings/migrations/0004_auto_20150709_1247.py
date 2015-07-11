# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0003_listing_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='expiry_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 11, 20, 47, 32, 939390)),
        ),
    ]
