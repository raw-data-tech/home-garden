# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('quantity', models.DecimalField(max_digits=5, decimal_places=2)),
                ('remark', models.CharField(max_length=256, null=True, blank=True)),
                ('status', model_utils.fields.StatusField(default=b'placed', max_length=100, no_check_for_status=True, choices=[(b'placed', b'placed'), (b'confirmed', b'confirmed'), (b'purchased', b'purchased'), (b'timedout', b'timedout'), (b'cancelled', b'cancelled'), (b'rejected', b'rejected')])),
                ('buyer', models.ForeignKey(related_name=b'orders', to=settings.AUTH_USER_MODEL)),
                ('listing', models.ForeignKey(related_name=b'orders', to='listings.Listing')),
            ],
            options={
                'ordering': ['-pk'],
            },
            bases=(models.Model,),
        ),
    ]
