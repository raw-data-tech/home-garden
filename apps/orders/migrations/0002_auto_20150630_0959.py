# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=model_utils.fields.StatusField(default=b'buyer_placed', max_length=100, no_check_for_status=True, choices=[(b'buyer_placed', b'buyer_placed'), (b'seller_confirmed', b'seller_confirmed'), (b'buyer_purchased', b'buyer_purchased'), (b'timedout', b'timedout'), (b'buyer_cancelled', b'buyer_cancelled'), (b'seller_rejected', b'seller_rejected')]),
        ),
    ]
