# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0006_auto_20150404_1116'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='activated',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ads',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 11, 28, 33, 103770, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 4, 11, 28, 33, 100990, tzinfo=utc)),
        ),
    ]
