# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0004_auto_20150404_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=20, choices=[(b'Toys', b'Toys'), (b'Candies', b'Candies'), (b'Fireworks', b'Fireworks')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 9, 34, 21, 929416, tzinfo=utc)),
        ),
    ]
