# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('rechan_shopping', '0010_auto_20150405_0209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 6, 9, 33, 15, 659021, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='product',
            name='publish_date',
            field=models.DateField(default=datetime.datetime(2015, 4, 6, 9, 33, 15, 655817, tzinfo=utc)),
        ),
    ]
