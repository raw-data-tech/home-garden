# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vegetable',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name_en', models.CharField(max_length=64, verbose_name=b'Name(English)')),
                ('name_ml', models.CharField(max_length=64, verbose_name=b'Name(Malayalam)')),
                ('image_url', models.URLField(null=True)),
                ('price_retail', models.PositiveIntegerField(null=True)),
                ('price_wholesale', models.PositiveIntegerField(null=True)),
                ('is_deleted', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
