# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('vegetables', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.DecimalField(max_digits=5, decimal_places=2)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('timeout_in_hours', models.PositiveSmallIntegerField(default=56)),
                ('is_cancelled', models.BooleanField(default=False)),
                ('seller', models.ForeignKey(related_name=b'listings', to=settings.AUTH_USER_MODEL)),
                ('vegetable', models.ForeignKey(related_name=b'listings', to='vegetables.Vegetable')),
            ],
            options={
                'ordering': ['-pk'],
            },
            bases=(models.Model,),
        ),
    ]
