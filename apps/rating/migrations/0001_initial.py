# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.PositiveIntegerField(verbose_name=b'rating', choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('remark', models.CharField(max_length=200, null=True, blank=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('order', models.ForeignKey(related_name=b'ratings', to='orders.Order')),
                ('user', models.ForeignKey(related_name=b'ratings', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
