# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0011_auto_20150406_1733'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 17, 6, 6, 43, 391364, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=20, choices=[(b'Toys', b'Toys'), (b'Candies', b'Candies'), (b'Lucky_draw', b'Lucky_draw')]),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 17, 6, 6, 43, 388214, tzinfo=utc)),
        ),
    ]
