# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0012_auto_20150417_1406'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='have',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ads',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 17, 7, 5, 41, 552448, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 17, 7, 5, 41, 547533, tzinfo=utc)),
        ),
    ]
